-- Solution to https://open.kattis.com/problems/conteststruggles
--
-- Problem C of NWERC 2020
--
-- 2024 Rudy Matela
--
-- quality: 3/6
-- difficulty: 2/6
-- topics:
-- * math
-- * paper
-- * golfable
--
-- Solve for x: (n-k)x + ks = nd
--
-- This solution is provided in code-golf form: 102 bytes.
main=interact$t.s.map read.words
s(n:k:d:s:_)=(n*d-k*s)/(n-k)
t p|0<=p&&p<=100=show p|0<1="impossible"
