import rasterio
import rasterio.features
import rasterio.warp
from geojson import Polygon, Feature, FeatureCollection, dump, dumps


def boundary():
  src = rasterio.open("RGB.byte.tif")
  print(src.shape)
  print(src.nodatavals)
  print(src.nodata)

  msk = src.read_masks(1)
  features = []

  for geom, val in rasterio.features.shapes(msk, transform=src.transform):
    geom = rasterio.warp.transform_geom(src.crs, 'EPSG:4326', geom, precision=6)
    if val == 255.0:
      features.append(Feature(geometry=geom))

  feature_collection = FeatureCollection(features)
  #Write to local disk
  #with open('output.geojson', 'w') as f:
  #  dump(feature_collection, f)
  
  return dumps(feature_collection, sort_keys=True)