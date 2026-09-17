# QA checklist

Run on the last 12 images at every 10-percent stop.

## Hard fail (must regenerate)

- Readable English or German word on the building (except the bottom catalog mark)
- Morr 56 or Garten shown with closed church doors
- Shallya as marble hospital or halo Madonna
- Sigmar 18 as cathedral or steeple church
- Ranald 6 or 57 as a chapel with a tower
- District fabric wrong (thatch street in Markt; cobble ring in Vorstadt; white lime in Schatten; coal soot on Markt gables)
- Object cut by the frame
- Wrong catalog number

## Soft fail (note, fix if user asks)

- Extra people in the foreground
- Neighbour buildings too rich or too poor for the district
- Missing a listed prop (tin bowl on 1, cabbage on 2, cart shaft on 3)
- Lighting too golden

## Pass line

Write `QA xx% | packs A–B | hard fails N | action`.
