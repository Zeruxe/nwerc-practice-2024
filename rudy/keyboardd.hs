-- Solution to https://open.kattis.com/problems/keyboardd
--
-- Problem K of NWERC 2020
--
-- 2024 Rudy Matela
--
-- quality: 3/6
-- difficulty: 2/6
-- topics:
-- * sets

import Data.List

main :: IO ()
main  =  interact $ (\[a,b] -> sticky a b ++ "\n") . take 2 . lines

sticky :: String -> String -> String
sticky cs ds  =  [ head a
                 | (a,b) <- zip (group (sort cs)) (group (sort ds))
                 , length b > length a
                 ]
