imax = 0
imin = 0
nums = []

while True:
    num = input("Enter a number:")
    if num == 'done':
        break
    else:
        try:
            num = float(num)
            nums.append(num)
        except:
            print("Invalid input!")

for i in nums:
    imax = int(max(nums))
    imin = int(min(nums))
print(imax,   imin)