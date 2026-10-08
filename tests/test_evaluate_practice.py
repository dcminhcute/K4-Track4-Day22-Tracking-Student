"""Kiểm tra tiến trình chấm nhận được alias NumPy và tham số video luyện."""

from evaluate_practice import run_trackeval


def test_run_trackeval_patches_numpy_in_child(tmp_path):
    """Tiến trình con dùng được alias và chỉ nhận video_1."""
    scripts = tmp_path / "scripts"
    scripts.mkdir()
    (scripts / "run_mot_challenge.py").write_text(
        "import sys\n"
        "import os\n"
        "import numpy as np\n"
        "assert np.float is float\n"
        "assert np.int is int\n"
        "assert os.environ['MPLBACKEND'] == 'Agg'\n"
        "assert sys.argv[0].endswith('run_mot_challenge.py')\n"
        "assert sys.argv[sys.argv.index('--SEQ_INFO') + 1] == 'video_1'\n"
        "assert sys.argv[sys.argv.index('--TRACKERS_TO_EVAL') + 1] == 'kiem_tra'\n",
        encoding="utf-8",
    )
    run_trackeval(tmp_path, "kiem_tra", "LAB21", "train")
