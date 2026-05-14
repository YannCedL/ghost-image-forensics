# test des fonctions forensics EXIF et ELA de Ghost
from ghost_image_forensics.exif import read_exif
from ghost_image_forensics.ela import run_ela

def test_exif_et_ela():
    contract = read_exif("test.jpg")
    assert contract is not None
    assert contract.result["camera_model"] is not None
    assert len(contract.evidence) >= 1

    ela = run_ela("test.jpg")
    assert "ela_score" in ela
    assert "verdict" in ela
