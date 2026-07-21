# Smart Public Grievance Management System - Raw Dataset Summary

Prepare a clean and organized raw image dataset for future YOLOv8 annotation and training.

## Dataset Balance Status

| Class | Number of Images |
|-------|------------------|
| Pothole | 105 |
| Electricity | 105 |
| Water-leakage | 105 |

**Total Images:** 315

---

## Quality Control (QC) Process

Our dataset pipeline incorporates several automated and validation filters to ensure high dataset fidelity:
1. **Size Verification:** Discarded all thumbnail images smaller than 10KB (often blurry or pixelated).
2. **Format/Corruption Checking:** Every download was fed to Pillow (PIL) for structural integrity validation. Any image that could not be successfully loaded or verified was discarded as corrupt/faulty.
3. **Exact Duplicate Removal:** Computed MD5 checksums of the binary data for all downloaded files. Exact duplicate images were removed to avoid bias, leakage, and overfitting.
4. **Keyword Specificity:** Focused searches using descriptive civic infrastructure terms (e.g. *damaged streetlight pole*, *fallen electrical pole*, *burst main water line*, *asphalt road pothole*).

### Quality Control Stats
- **Total Unique Images Collected:** 315
- **Invalid/Corrupt/Low-res Ignored:** Total of hundreds of non-conforming items automatically skipped.
- **Deduplicated Items:** Duplicate matches identified by MD5 hashing and excluded.

---

## Known Dataset Limitations

1. **Resolution Variation:** The gathered images have varied resolution and aspect ratios, coming from real-world online platforms.
2. **Multi-label Occurrences:** Some images categorized as *electricity* or *water-leakage* might also contain road defects (e.g., a burst pipe causing road damage). Annotators should flag these carefully.
3. **Domain Shift:** Since images are crawled globally, urban environments, road colors, and utility poles may vary compared to specific local municipal regions.

---

## Image Source Information & URL Log

Below is the log of source domains and unique files generated dynamically:

### Pothole Source Log (Selected samples)
| File | Source Domain | Source URL |
| --- | --- | --- |
| pothole_001.jpg | png.pngtree.com | https://png.pngtree.com/thumb_back/fh260/background/20250320/pngtree-close-up-of-a-pothole-on-an-asphalt-road-with-car-image_17110686.jpg |
| pothole_002.jpg | thumbs.dreamstime.com | https://thumbs.dreamstime.com/z/road-pit-close-up-asphalt-pothole-need-to-repair-338792575.jpg?w=992 |
| pothole_003.jpg | thumbs.dreamstime.com | https://thumbs.dreamstime.com/b/close-up-view-pothole-cracked-asphalt-road-roadway-surface-shows-damage-deterioration-puddle-reflects-sky-road-close-up-view-358206686.jpg |
| pothole_004.jpg | thumbs.dreamstime.com | https://thumbs.dreamstime.com/b/pothole-scenic-road-car-distance-sunset-close-up-image-pothole-filled-water-scenic-road-333097752.jpg |
| pothole_005.jpg | c8.alamy.com | https://c8.alamy.com/comp/2M52FXK/close-up-of-big-pothole-with-dirty-rain-water-of-the-road-2M52FXK.jpg |
| pothole_006.jpg | thumbs.dreamstime.com | https://thumbs.dreamstime.com/b/close-up-asphalt-road-damaged-surface-deep-pothole-daylight-close-up-view-asphalt-road-significant-399842626.jpg |
| pothole_007.jpg | thumbs.dreamstime.com | https://thumbs.dreamstime.com/z/close-up-cracked-asphalt-road-dangerous-pothole-road-thaialnd-84710106.jpg |
| pothole_008.jpg | thumbs.dreamstime.com | https://thumbs.dreamstime.com/b/close-up-asphalt-road-featuring-pothole-filled-rainwater-surface-visibly-cracked-around-pothole-water-399843742.jpg?w=992 |
| pothole_009.jpg | thumbs.dreamstime.com | https://thumbs.dreamstime.com/b/close-up-shot-pothole-damaged-asphalt-road-deep-hole-water-puddle-black-cracked-pavement-destruction-deterioration-385717410.jpg?w=992 |
| pothole_010.jpg | static.vecteezy.com | https://static.vecteezy.com/system/resources/previews/073/057/793/large_2x/close-up-view-of-a-large-deep-pothole-on-a-cracked-asphalt-road-with-broken-pavement-pieces-scattered-around-the-edges-photo.jpg |
| pothole_011.jpg | png.pngtree.com | https://png.pngtree.com/thumb_back/fw800/background/20250324/pngtree-close-up-of-a-pothole-on-an-asphalt-road-with-car-image_17136087.jpg |
| pothole_012.jpg | c8.alamy.com | https://c8.alamy.com/comp/2J9WEA0/asphalt-swelling-close-up-pothole-and-pit-on-road-2J9WEA0.jpg |
| pothole_013.jpg | c8.alamy.com | https://c8.alamy.com/comp/DP2TN3/close-up-of-pothole-potholes-in-the-road-in-winter-england-uk-united-DP2TN3.jpg |
| pothole_014.jpg | c8.alamy.com | https://c8.alamy.com/comp/DP2TC1/close-up-of-deep-large-pothole-potholes-in-the-road-filled-with-water-DP2TC1.jpg |
| pothole_015.jpg | thumbs.dreamstime.com | https://thumbs.dreamstime.com/z/road-pothole-flooded-board-water-close-up-background-texture-road-pothole-flooded-board-water-close-up-background-168996852.jpg |
| pothole_016.jpg | c8.alamy.com | https://c8.alamy.com/comp/2EM5FT4/pothole-or-pot-hole-damage-in-road-surface-2EM5FT4.jpg |
| pothole_017.jpg | c8.alamy.com | https://c8.alamy.com/comp/2F58J08/close-up-of-a-pothole-on-a-quiet-country-tarmac-road-in-rural-devon-england-uk-2F58J08.jpg |
| pothole_018.jpg | c8.alamy.com | https://c8.alamy.com/comp/BM0XR0/close-up-of-a-pot-hole-in-a-suburban-road-in-hounslow-middx-uk-may-BM0XR0.jpg |
| pothole_019.jpg | c8.alamy.com | https://c8.alamy.com/comp/B08K7H/close-up-of-a-pothole-in-the-streets-B08K7H.jpg |
| pothole_020.jpg | png.pngtree.com | https://png.pngtree.com/thumb_back/fh260/background/20250320/pngtree-close-up-of-a-pothole-on-an-asphalt-road-with-car-image_17120297.jpg |
| ... | and 85 more sources | ... |

### Electricity Source Log (Selected samples)
| File | Source Domain | Source URL |
| --- | --- | --- |
| electricity_001.jpg | thumbs.dreamstime.com | https://thumbs.dreamstime.com/z/broken-traffic-light-pole-pedestrian-crossing-accident-damaged-lies-highlighting-urban-decay-road-safety-issues-347413479.jpg |
| electricity_002.jpg | c8.alamy.com | https://c8.alamy.com/comp/2PW8HEE/file-photo-dated-140720-of-a-damaged-street-light-as-more-than-200000-streetlights-were-reported-as-broken-last-year-with-some-lamps-taking-years-to-fix-according-to-liberal-democrat-research-2PW8HEE.jpg |
| electricity_003.jpg | thumbs.dreamstime.com | https://thumbs.dreamstime.com/b/lightpole-copper-theft-damaged-street-lights-selective-focus-vintage-style-86325460.jpg |
| electricity_004.jpg | thumbs.dreamstime.com | https://thumbs.dreamstime.com/b/broken-traffic-light-accident-street-77015701.jpg |
| electricity_005.jpg | thumbs.dreamstime.com | https://thumbs.dreamstime.com/b/damaged-traffic-light-pole-city-pedestrian-crossing-broken-traffic-light-pole-lie-pedestrian-crossing-347470520.jpg |
| electricity_006.jpg | c8.alamy.com | https://c8.alamy.com/comp/2Y5Y4N2/an-old-deteriorated-street-lamp-from-ddr-times-the-damaged-concrete-pole-and-worn-out-light-fixture-highlight-the-need-for-modernization-2Y5Y4N2.jpg |
| electricity_007.jpg | c8.alamy.com | https://c8.alamy.com/comp/2AJAMEW/old-broken-street-lamp-streetlight-and-dirty-roll-down-shutters-in-dilapidated-suburb-deteriorated-urban-residential-district-2AJAMEW.jpg |
| electricity_008.jpg | c8.alamy.com | https://c8.alamy.com/comp/BGA826/broken-street-lamp-in-a-wooden-pole-BGA826.jpg |
| electricity_009.jpg | thumbs.dreamstime.com | https://thumbs.dreamstime.com/z/traffic-accident-site-broken-traffic-lights-pole-lying-pedestrian-crossing-busy-urban-street-cars-visible-347470527.jpg |
| electricity_010.jpg | bloximages.chicago2.vip.townnews.com | https://bloximages.chicago2.vip.townnews.com/pharostribune.com/content/tncms/assets/v3/editorial/1/c4/1c4e532a-a1da-11e5-aa6f-eb0208506ad9/566dd9151787a.image.jpg?resize=1200%2C900 |
| electricity_011.jpg | thumbs.dreamstime.com | https://thumbs.dreamstime.com/z/broken-traffic-light-pole-leaning-city-intersection-damaged-over-pedestrian-crossing-busy-street-captures-urban-decay-345038504.jpg |
| electricity_012.jpg | c2.staticflickr.com | https://c2.staticflickr.com/4/3618/3383458014_d7850bddb2_b.jpg |
| electricity_013.jpg | c8.alamy.com | https://c8.alamy.com/comp/B0XF8G/pink-clouds-behind-a-fallen-branch-and-streetlight-pole-with-destroyed-B0XF8G.jpg |
| electricity_014.jpg | www.shutterstock.com | https://www.shutterstock.com/image-photo/detail-shot-broken-street-lamp-600nw-334237046.jpg |
| electricity_015.png | images.gmanews.tv | https://images.gmanews.tv/regionaltv2023/content_images/article/BANNERCMSONCLKIDLATE_2024_06_06_20_52_47.png |
| electricity_016.jpg | i2-prod.kentlive.news | https://i2-prod.kentlive.news/incoming/article8398468.ece/ALTERNATES/s810/0_Faulty-streetlights.jpg |
| electricity_017.jpg | images.squarespace-cdn.com | https://images.squarespace-cdn.com/content/v1/5522ceeae4b0593541222134/1474994337564-GQ4JYQSKSEIJBQQ7AI9G/image-asset.jpeg?format=2500w |
| electricity_018.jpg | www.hindustantimes.com | https://www.hindustantimes.com/ht-img/img/2023/06/23/1600x900/A-slanting-streetlight-pole-in-Ludhiana-on-Friday-_1687544398608.jpg |
| electricity_019.jpg | thumbs.dreamstime.com | https://thumbs.dreamstime.com/z/city-crew-replacing-storm-damaged-streetlight-poles-neighborhood-city-crew-replacing-storm-damaged-streetlight-poles-348999000.jpg |
| electricity_020.jpg | i2-prod.kentlive.news | https://i2-prod.kentlive.news/incoming/article8398468.ece/ALTERNATES/s1200c/0_Faulty-streetlights.jpg |
| ... | and 85 more sources | ... |

### Water-leakage Source Log (Selected samples)
| File | Source Domain | Source URL |
| --- | --- | --- |
| water-leakage_001.jpg | punemirror.com | https://punemirror.com/wp-content/uploads/2026/01/sb-road-pipeline-burst-1044x653.webp |
| water-leakage_002.jpg | d3pc1xvrcw35tl.cloudfront.net | https://d3pc1xvrcw35tl.cloudfront.net/ln/images/1200x900/pipeline-burst-near-bandra_2026021070736.jpg |
| water-leakage_003.jpg | thumbs.dreamstime.com | https://thumbs.dreamstime.com/b/image-png-441038607.jpg?w=576 |
| water-leakage_004.png | images.timesnownews.com | https://images.timesnownews.com/thumb/msid-152939010,thumbsize-936982,width-1280,height-720,resizemode-75/152939010.jpg |
| water-leakage_005.jpg | www.incrediblegoa.org | https://www.incrediblegoa.org/wp-content/uploads/2019/08/Another-Pipeline-Burst.jpg |
| water-leakage_006.jpg | thumbs.dreamstime.com | https://thumbs.dreamstime.com/b/water-pipe-line-burst-road-caved-drinking-pipeline-flow-stopped-help-loader-166083293.jpg |
| water-leakage_007.jpg | thumbs.dreamstime.com | https://thumbs.dreamstime.com/b/water-gushing-hose-draining-puddle-demolished-urban-street-pipeline-repair-burst-pipe-road-construction-rainy-day-427422727.jpg |
| water-leakage_008.jpg | i.ytimg.com | https://i.ytimg.com/vi/FMMoWY0FJFI/maxresdefault.jpg?sqp=-oaymwEmCIAKENAF8quKqQMa8AEB-AH-CYAC0AWKAgwIABABGGUgXChSMA8=&amp;rs=AOn4CLBJD49QHWgY-8xGveT8Ftqis_Uk-w |
| water-leakage_009.jpg | ichef.bbci.co.uk | https://ichef.bbci.co.uk/ace/standard/976/cpsprodpb/9E21/production/_101918404_burstpipe.jpg |
| water-leakage_010.jpg | www.mumbailive.com | https://www.mumbailive.com/images/media/images/fountain_1722845523226.jpg?bg=373936&amp;crop=485%2C272.280701754386%2C0%2Cnull&amp;fit=crop&amp;fitToScale=w%2C1368%2C768&amp;fm=webp&amp;h=606.3157894736842&amp;height=309&amp;w=1080&amp;width=485 |
| water-leakage_011.jpg | www.livehindustan.com | https://www.livehindustan.com/lh-img/smart/img/smart/2025/12/11/1600x900/logo/11321011MR_M_36_11122025_36_1765476280692.JPG |
| water-leakage_012.jpg | thumbs.dreamstime.com | https://thumbs.dreamstime.com/b/water-bursts-damaged-industrial-pipeline-massive-water-stream-broken-pipe-accident-water-supply-system-pipeline-water-385014449.jpg |
| water-leakage_013.jpg | images.timesnownews.com | https://images.timesnownews.com/thumb/msid-115946051,thumbsize-46298,width-1280,height-720,resizemode-75/115946051.jpg |
| water-leakage_014.jpg | media.assettype.com | https://media.assettype.com/freepressjournal/2025-12-06/c42ckq8u/1000391455.jpg?width=1200 |
| water-leakage_015.jpg | c8.alamy.com | https://c8.alamy.com/comp/RHF3XD/burst-water-main-pipe-in-a-main-road-RHF3XD.jpg |
| water-leakage_016.jpg | thecsrjournal.in | https://thecsrjournal.in/wp-content/uploads/2026/04/water-pipeline-burst.webp |
| water-leakage_017.jpg | img.freepik.com | https://img.freepik.com/premium-vector/broken-city-water-pipe-pipeline-burst-break-plumbing-concept-flat-graphic-design-illustration_133260-7466.jpg?w=740 |
| water-leakage_018.jpg | media.assettype.com | https://media.assettype.com/freepressjournal/2026-06-03/sw6ah510/Untitled-design-2026-06-03T161127.864.jpg |
| water-leakage_019.jpg | st1.latestly.com | https://st1.latestly.com/wp-content/uploads/2024/03/100-2-1-784x441.jpg |
| water-leakage_020.jpg | static.vecteezy.com | https://static.vecteezy.com/system/resources/previews/012/684/089/non_2x/burst-pipe-water-pouring-pipeline-accident-it-s-dangerous-situation-photo.jpg |
| ... | and 85 more sources | ... |

