// 計算GPS兩點直線距離
// 可英哩、公里切換
//http://www.codecodex.com/wiki/Calculate_distance_between_two_points_on_a_globe

using System;
namespace HaversineFormula
{
    /// <summary>
    /// The distance type to return the results in.
    /// </summary>
    public enum DistanceType { Miles, Kilometers };
    /// <summary>
    /// Specifies a Latitude / Longitude point.
    /// </summary>
    public struct Position
    {
        public double Latitude;
        public double Longitude;
    }
    class Haversine
    {
        /// <summary>
        /// Returns the distance in miles or kilometers of any two
        /// latitude / longitude points.
        /// </summary>
        /// <param name=”pos1〃></param>
        /// <param name=”pos2〃></param>
        /// <param name=”type”></param>
        /// <returns></returns>
        public double Distance(Position pos1, Position pos2, DistanceType type)
        {
            double R = (type == DistanceType.Miles) ? 3960 : 6371;
            double dLat = this.toRadian(pos2.Latitude - pos1.Latitude);
            double dLon = this.toRadian(pos2.Longitude - pos1.Longitude);
            double a = Math.Sin(dLat / 2) * Math.Sin(dLat / 2) +
                Math.Cos(this.toRadian(pos1.Latitude)) * Math.Cos(this.toRadian(pos2.Latitude)) *
                Math.Sin(dLon / 2) * Math.Sin(dLon / 2);
            double c = 2 * Math.Asin(Math.Min(1, Math.Sqrt(a)));
            double d = R * c;
            return d;
        }
        /// <summary>
        /// Convert to Radians.
        /// </summary>
        /// <param name="val"></param>
        /// <returns></returns>
        private double toRadian(double val)
        {
            return (Math.PI / 180) * val;
        }
    }
}

// To use this code you will need 2 latitude/longitude points.  I created a struct to hold the  latitude/longitude points.  Once we have the points, we create the Haversine class and call the Distance method, passing in the points and an enum specifying whether to return the results in Kilometers or Miles.  We end up with the following:

// Position pos1 = new Position();
// pos1.Latitude = 40.7486;
// pos1.Longitude = -73.9864;
// Position pos2 = new Position();
// pos2.Latitude = 24.7486;
// pos2.Longitude = -72.9864;
// Haversine hv = new Haversine();
// double result = hv.Distance(pos1, pos2, DistanceType.Kilometers);