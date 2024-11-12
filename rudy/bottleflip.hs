-- Solution to https://open.kattis.com/problems/bottleflip
--
-- Problem B from NWERC 2022
--
-- 2023 Rudy Matela
--
-- quality: 3/6
-- difficulty: 3/6
-- topics:
-- * maths
-- * physics
-- * geometry
-- * paper

import Debug.Trace

-- | centre of mass
--
-- Usage:
--
-- > > centre dair dwater height
--
-- With the density of air,
-- density of water,
-- and proportional height (0-1) of the water.
--
-- > > centre 1 4 (2/3)
-- > 0.43  -- 13 % 30
--
-- > > centre 2 3 (1/2)
-- > 0.45  -- 9 % 20
--
-- > > centre 1 2 0
-- > 0.5
--
-- > > centre 1 2 0.5
-- > 0.4166666666666667
--
-- > > centre 1 2 1
-- > 0.5
centre :: (Show a, Fractional a) => a -> a -> a -> a
centre da dw hw  =  (ca * ma + cw * mw) / (ma + mw)
  where
  ha  =  1 - hw
  ca  =  ha / 2 + hw
  cw  =  hw / 2
  ma  =  ha * da
  mw  =  hw * dw


centre2 :: (Show a, Fractional a) => a -> a -> a -> a
centre2 a w h  =  (a - a * h * h + h * h * w)
               /  (2 * a - 2 * h * a + 2 * h * w)


-- It seems to be that the minimum centre is always at
-- where the centre of mass lays exactly at the edge of the water
-- so it is just a matter of solving an equation for X.
bruteMinimumCentre :: (Show a, Ord a, Enum a, Fractional a) => a -> a -> (a,a)
bruteMinimumCentre da dw  =  minimum
  [(centre da dw h, h) | h <- [0.0000, 0.0001 .. 1.0000]]


-- minimumCentre1 :: (Floating a, Fractional a) => a -> a -> a
-- minimumCentre1 a w  =  (-2 * a + sqrt (4 * a * a + 4 * a * (w - a)))
--                     /  (2 * (w - a))

minimumCentre :: (Floating a, Fractional a) => a -> a -> a
minimumCentre a w  =  pos
  where
  pos  =  (-a + sqrt (a * w)) / (w - a)
  neg  =  (-a - sqrt (a * w)) / (w - a) -- will always be negative, we don't want


main :: IO ()
main  =  interact (unlines . map (show . solve . map read . words) . lines)

solve :: [Double] -> Double
solve [h,r,a,w]  =  minimumCentre a w * h
