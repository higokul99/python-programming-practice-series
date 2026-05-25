class Math:
    def add(self, *nums):
        return sum(nums)
    

m = Math()
print(m.add(10,2))
print(m.add(10,11))


class Team:
    def __len__(self):
        return 5
    
tm = Team()
print(len(tm))