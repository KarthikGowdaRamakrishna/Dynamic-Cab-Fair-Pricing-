## Dynamic Cab Fair Pricing Strategy

### Project Overview

This project applies data science techniques to develop a dynamic pricing model for cab fares, aiming to optimize revenue and enhance customer satisfaction. Utilizing a combination of historical data analysis and real-time demand assessment, the model adjusts prices based on current market conditions.

The application is hosted on Streamlit, allowing users to interact with the pricing model and understand how different factors influence cab fares. Check out the live app: [Dynamic Cab Fair Pricing Strategies](https://dynamic-cab-fair-pricing-strats.streamlit.app/)

### Scalability and Enhanced Strategy

The model can be scaled and refined by implementing a zonal analysis strategy. By defining zones with certain radii and querying the number of riders and drivers within these zones, the pricing strategy can be more precisely tailored to local demand and supply conditions. This approach can dynamically adjust cab fares and direct resources more efficiently.

#### Sample SQL Query for Zonal Data Analysis

This SQL query demonstrates how to extract the count of riders and drivers within a specific zone, defined by a geographical radius around a central point (latitude and longitude).

```sql
SELECT 
  zone_id,
  COUNT(DISTINCT rider_id) AS number_of_riders,
  COUNT(DISTINCT driver_id) AS number_of_drivers
FROM 
  trips
WHERE 
  ST_DistanceSphere(point(longitude, latitude), point(:central_lon, :central_lat)) <= :radius
GROUP BY 
  zone_id;
```

This query utilizes the `ST_DistanceSphere` function to calculate the spherical distance between a predefined central point and the locations in the `trips` table. `:radius` is the radius of the zone in meters, and `:central_lat`, `:central_lon` are the coordinates of the zone center.

### How to Use the App

1. **Visit the App**: Navigate to [Dynamic Cab Fair Pricing Strategies](https://dynamic-cab-fair-pricing-strats.streamlit.app/).
2. **Input Data**: Enter data such as number of riders, drivers, vehicle type, and expected ride duration.
3. **View Results**: The app will display the dynamically calculated fare based on the input and current demand within the specified zones.

### Future Enhancements

Further enhancements could include integrating live traffic data, weather conditions, and special event schedules to refine pricing predictions and improve service delivery during peak times.

### Feedback

I value your feedback to improve the app and its functionalities. Please visit the app and provide your insights and suggestions.
