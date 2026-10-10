import importlib.util
import json
import os
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch
import yaml

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts/lib"))
import state
spec = importlib.util.spec_from_file_location("foundation_renderer", ROOT / "infrastructure/render.py")
renderer = importlib.util.module_from_spec(spec)
spec.loader.exec_module(renderer)


class ContractTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.home = Path(self.temp.name).resolve()
        self.home_patch = patch.object(Path, "home", return_value=self.home)
        self.home_patch.start()
        self.env_patch = patch.dict(os.environ, {}, clear=False)
        self.env_patch.start()
        os.environ.pop("LAB_STATE_DIR", None)
        os.environ.pop("SUDO_UID", None)

    def tearDown(self):
        self.env_patch.stop()
        self.home_patch.stop()
        self.temp.cleanup()

    def test_foundation_prepares_no_observability_secrets(self):
        path = state.prepare_foundation()
        renderer.render()
        kind = yaml.safe_load((path / "rendered/foundation-kind.yaml").read_text())
        self.assertTrue(kind["networking"]["disableDefaultCNI"])
        self.assertEqual(2, len(kind["nodes"]))
        self.assertFalse((path / "credentials.json").exists())
        self.assertFalse((path / "rendered/grafana.yaml").exists())

    def test_handoff_rejects_owner_and_version_changes(self):
        path = state.prepare_foundation()
        (path / "kubeconfig").write_text("test only")
        (path / "foundation.json").write_text(json.dumps(state.foundation_manifest()))
        state.check_foundation()
        recorded = json.loads((path / "foundation.json").read_text())
        recorded["versions_sha256"] = "wrong"
        (path / "foundation.json").write_text(json.dumps(recorded))
        with self.assertRaises(ValueError): state.check_foundation()
        (path / "foundation.json").write_text(json.dumps(state.foundation_manifest()))
        owner = json.loads((path / "owner.json").read_text())
        owner["id"] = "b60388bc-9443-4f45-948f-7a8ae12e6d55"
        (path / "owner.json").write_text(json.dumps(owner))
        with self.assertRaises(ValueError): state.check_foundation()

    def test_followup_prepare_preserves_and_destroy_removes_all(self):
        path = state.prepare()
        credentials = (path / "credentials.json").read_bytes()
        (path / "nodes/worker/grafana/db").write_text("dashboard")
        (path / "nodes/worker/seaweedfs/object").write_text("trace and log blocks")
        state.prepare_foundation()
        state.prepare()
        self.assertEqual(credentials, (path / "credentials.json").read_bytes())
        self.assertEqual("dashboard", (path / "nodes/worker/grafana/db").read_text())
        state.destroy_data()
        self.assertFalse(path.exists())
        state.destroy_data()

    def test_unowned_state_and_noncanonical_paths_are_refused(self):
        for path in (self.home, self.home / "other", Path("relative")):
            os.environ["LAB_STATE_DIR"] = str(path)
            with self.assertRaises(ValueError): state.state_path()
        os.environ.pop("LAB_STATE_DIR")
        path = state.state_path()
        path.mkdir(parents=True)
        (path / "unrelated").write_text("keep")
        with self.assertRaises(ValueError): state.destroy_data()
        self.assertTrue((path / "unrelated").exists())

if __name__ == "__main__": unittest.main()
