def you_either_know():
    input_bytes_as_hex = "0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104"
    input_bytes_as_ascii_nums = [byte for byte in bytes.fromhex(input_bytes_as_hex)] # zrobienie z ciagu bitow listy znakow ascii

    # 42 bajty sa w tym input string
    print(input_bytes_as_ascii_nums)

    # pierwsze 7 bajtów klucza to myXORke
    key = [109, 121, 88, 79, 82, 107, 101, 121]*6 #wydluzenie klucza 6krotnie, 7*6=42
    print(key)

    output = []
    for i in range(42):
        output.append(chr(input_bytes_as_ascii_nums[i] ^ key[i]))

    print(output)

    out = "".join(i for i in output)
    print(out)


# from pwn import xor
# flag = bytes.fromhex('0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104')
# print(xor(flag, 'crypto{'.encode())) # oh, it says 'myXORke+y...'
# print(xor(flag, 'myXORkey'.encode())) # try this? yay, it works! sometimes simpler is better