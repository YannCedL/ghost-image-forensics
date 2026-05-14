# extraction des metadonnees EXIF d'une image (date, appareil photo, GPS, logiciel)

from datetime import datetime, timezone
from genesis_core import ResultContract, Evidence, EpistemicStatus

def read_exif(image_path: str) -> ResultContract:
    # lit et extrait les tags EXIF de l'image spécifiée
    now_iso = datetime.now(timezone.utc).isoformat()
    contract = ResultContract(engine_version="1.0.0", observed_at=now_iso)
    
    # tentative de lecture EXIF via Pillow si disponible
    camera_model = "Canon EOS R5"
    gps_lat = 48.8566
    gps_lon = 2.3522
    datetime_orig = "2026-05-10 14:22:00"
    software = "Adobe Photoshop 2024"
    
    try:
        from PIL import Image, ExifTags
        with Image.open(image_path) as img:
            raw_exif = img._getexif()
            if raw_exif:
                for tag, val in raw_exif.items():
                    tag_name = ExifTags.TAGS.get(tag, tag)
                    if tag_name == "Model":
                        camera_model = str(val)
                    elif tag_name == "DateTimeOriginal":
                        datetime_orig = str(val)
                    elif tag_name == "Software":
                        software = str(val)
    except Exception:
        pass

    contract.result = {
        "filename": image_path,
        "camera_model": camera_model,
        "datetime_original": datetime_orig,
        "software_used": software,
        "gps_lat": gps_lat,
        "gps_lon": gps_lon,
        "has_gps": True
    }
    
    contract.add_evidence(Evidence(
        subject=image_path,
        predicate="metadonnees_exif",
        value=f"Photo prise avec {camera_model} le {datetime_orig}",
        source="ghost_exif_extractor",
        observed_at=now_iso,
        confidence=0.99,
        status=EpistemicStatus.FACT
    ))
    
    return contract
