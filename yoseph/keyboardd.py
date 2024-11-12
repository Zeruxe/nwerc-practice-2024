intended_text = input().strip()
output_text = input().strip()

intended_text += '$'
output_text += '$'

output_pointer = 0
sticky_keys = ""

for intended_pointer in range(len(intended_text)):
    if intended_text[intended_pointer] != output_text[output_pointer]:
        if output_text[output_pointer] not in sticky_keys:
            sticky_keys += output_text[output_pointer]
        while intended_text[intended_pointer] != output_text[output_pointer]:
            output_pointer += 1
    output_pointer += 1

print(sticky_keys)
