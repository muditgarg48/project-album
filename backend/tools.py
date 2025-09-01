from PIL.ExifTags import GPSTAGS

def convert_to_degrees(value):
    """Convert GPS coordinates stored as rationals to float degrees."""
    try:
        d, m, s = value
        return float(d[0]) / float(d[1]) + \
               (float(m[0]) / float(m[1])) / 60.0 + \
               (float(s[0]) / float(s[1])) / 3600.0
    except Exception:
        return None

def extract_gps_info(gps_info):
    """Extract and convert GPS latitude, longitude, altitude."""
    gps_data = {"Latitude": None, "Longitude": None, "Altitude": None}
    if not gps_info:
        return gps_data

    gps = {}
    for key, val in gps_info.items():
        decoded = GPSTAGS.get(key, key)
        gps[decoded] = val

    if "GPSLatitude" in gps and "GPSLatitudeRef" in gps:
        lat = convert_to_degrees(gps["GPSLatitude"])
        if lat is not None and gps["GPSLatitudeRef"] in ["S", b"S"]:
            lat = -lat
        gps_data["Latitude"] = lat

    if "GPSLongitude" in gps and "GPSLongitudeRef" in gps:
        lon = convert_to_degrees(gps["GPSLongitude"])
        if lon is not None and gps["GPSLongitudeRef"] in ["W", b"W"]:
            lon = -lon
        gps_data["Longitude"] = lon

    if "GPSAltitude" in gps and "GPSAltitudeRef" in gps:
        try:
            alt = float(gps["GPSAltitude"][0]) / float(gps["GPSAltitude"][1])
            if gps["GPSAltitudeRef"] == 1:
                alt = -alt
            gps_data["Altitude"] = alt
        except Exception:
            gps_data["Altitude"] = None

    return gps_data