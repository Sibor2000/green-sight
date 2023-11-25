# Datasets

This file contains handpicked datasets that are used in the book.

## Data

### Districts and Administrative Regions

```
[out:json];

// Define the area for Berlin
area["name"="Berlin"][admin_level=4]->.berlin;

// Extract districts within Berlin with geometry
rel(area.berlin)["admin_level"="9"];
out geom;

// Output the results
out meta;
```