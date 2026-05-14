from ghost_image_forensics import read_exif, run_ela

def test_read_exif():
    c = read_exif("photo.jpg")
    assert "gps_lat" in c.result
    assert c.confidence > 0.9

def test_run_ela():
    r = run_ela("photo.jpg")
    assert r["verdict"] == "likely_authentic"
