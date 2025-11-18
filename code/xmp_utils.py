"""Utilities for parsing XMP metadata from images.

This module provides a QGIS-independent get_flight_yaw(photo_path) helper that
returns a float yaw (0-360) when FlightYawDegree is present in XMP, otherwise
returns None.
"""
from typing import Optional
import xml.etree.ElementTree as ET


def get_flight_yaw(photo_path: str) -> Optional[float]:
    """Extract FlightYawDegree from XMP block inside the image file.

    Returns yaw in degrees normalized to [0, 360), or None if not found/parse error.
    This function intentionally avoids QGIS imports so it can be unit-tested.
    """
    try:
        with open(photo_path, 'rb') as f:
            content = f.read()

        start = content.find(b"<x:xmpmeta")
        end = content.find(b"</x:xmpmeta>")
        if start == -1 or end == -1:
            return None

        xmp_data = content[start:end + len(b"</x:xmpmeta>")]
        xml = xmp_data.decode('utf-8', errors='ignore')
        root = ET.fromstring(xml)

        ns = {
            'drone-dji': 'http://www.dji.com/drone-dji/1.0/',
            'rdf': 'http://www.w3.org/1999/02/22-rdf-syntax-ns#'
        }

        for desc in root.findall('.//rdf:Description', ns):
            yaw = desc.attrib.get('{http://www.dji.com/drone-dji/1.0/}FlightYawDegree')
            if yaw is not None:
                try:
                    # Replace comma decimal separators sometimes found in metadata
                    value = float(str(yaw).replace(',', '.'))
                    return value % 360
                except Exception:
                    return None
        return None
    except Exception:
        return None

