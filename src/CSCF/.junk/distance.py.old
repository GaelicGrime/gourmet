

def vGreatCircleDistance(lat1, lon1, lat2=40.687088, lon2=-111.927630, earthRadius=6371):  # 3959 for miles 6371 for km
  # convert from degrees to radians
  latFrom = math.radians(lat1)
  lonFrom = math.radians(lon1)
  latTo = math.radians(lat2)
  lonTo = math.radians(lon2)

  lonDelta = lonTo - lonFrom
  a = pow(math.cos(latTo) * math.sin(lonDelta), 2) + pow(math.cos(latFrom) * math.sin(latTo) - math.sin(latFrom) * math.cos(latTo) * math.cos(lonDelta), 2)
  b = math.sin(latFrom) * math.sin(latTo) + math.cos(latFrom) * math.cos(latTo) * math.cos(lonDelta)

  angle = math.atan2(math.sqrt(a), b)
  return angle * earthRadius



def GCdistance(lat1, lon1, lat2, lon2, unit):
  theta = lon1 - lon2
  sinRadLat2 = math.sin(math.radians(lat2))
  cosRadLat2 = math.cos(math.radians(lat2))
  cosRadLat1 = math.cos(math.radians(lat1))
  sinRadLat1 = math.sin(math.radians(lat1))
  cosRadTheta = math.cos(math.radians(theta))
  dist = sinRadLat1 * sinRadLat2 + cosRadLat1 * cosRadLat2 * cosRadTheta
  dist = math.cos(dist)
  dist = math.degrees(dist)


d=acos(cos(radian(90-lat1))*cos(radian(90-lat2))+sin(radian(90-lat1))*sin(radian(90-lat2)*cos(radian(long1-long2)))*3959
