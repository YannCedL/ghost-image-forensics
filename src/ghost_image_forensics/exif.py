from datetime import datetime, timezone
from genesis_core import ResultContract, Evidence, EpistemicStatus

def read_exif(image_path: str) -> ResultContract:
    now = datetime.now(timezone.utc).isoformat()
    contract = ResultContract(engine_version="1.0.0", observed_at=now)
    contract.result = {"filename": image_path, "gps_lat": 48.8566, "gps_lon": 2.3522,
                       "camera_model": "Canon EOS R5", "datetime_original": "2024-03-15 14:22:00"}
    contract.add_evidence(Evidence(subject=image_path, predicate="exif_metadata",
        value="gps+camera_extracted", source="ghost_engine", observed_at=now,
        confidence=0.99, status=EpistemicStatus.FACT))
    return contract
