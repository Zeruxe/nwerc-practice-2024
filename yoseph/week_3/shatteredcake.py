width_original = int(input())
num_pieces = int(input())

total_area = 0
for _ in range(num_pieces):
    width_piece, length_piece = map(int, input().split())
    total_area += width_piece * length_piece

length_original = total_area // width_original

print(length_original)
