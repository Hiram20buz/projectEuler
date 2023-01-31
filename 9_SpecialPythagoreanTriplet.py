https://stackoverflow.com/questions/42752743/check-if-three-numbers-can-form-a-pythagorean-triple
nums = []

for num in range(0,3):
    nums.append(int(input("Enter a number")))

if ((nums[0] ** 2) + (nums[1] ** 2) == (nums[2] ** 2)):
    print(True)
    
if ((nums[0] ** 2) + (nums[1] ** 2) == (1000-nums[0]-nums[1])** 2):
    print(True)
