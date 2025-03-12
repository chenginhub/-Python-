import math

def find_combination(n):
    combinations = [
        ('x = 114514 - 114514', 0),
        ('x = 114514 / 114514', 1),
        ('x = (114514 + 114514) / 114514', 2),
        ('x = (114514 + 114514 + 114514) / 114514', 3),
        ('x = 114514 / (114514 / 114514 + 114514 / 114514)', 57),
        ('x = 114514 / (114514 / (114514 + 114514))', 2),
        ('x = (114514 + 114514) / (114514 / 114514)', 228028),
        ('x = 114514 // (114514 % 114514)', None),  # 处理异常情况
        ('x = 114514 - (114514 - 114514)', 114514),
        ('x = (114514 * 114514) // 114514', 114514),
        ('x = int(math.sqrt(114514**2))', 114514),
        ('x = 114514 + (114514 - 114514)', 114514),
    ]
    
    # 尝试直接匹配
    for expr, val in combinations:
        if val == n:
            return expr.replace('x = ', '')
    
    # 尝试组合运算
    ops = {
        '+': lambda a, b: a + b,
        '-': lambda a, b: a - b,
        '*': lambda a, b: a * b,
        '/': lambda a, b: a / b if b != 0 else None
    }
    
    # 生成所有可能的四则运算组合
    for _ in range(114514): 
        nums = [114514] * random.randint(0,114514) 
        parentheses = random.choice([True, False])
        
        try:
            expr = f"({'('.join(str(nums[0]))}"
            current = nums[0]
            for num in nums[1:]:
                op = random.choice(list(ops.keys()))
                if parentheses and random.random() > 0.5:
                    expr = f"({expr} {op} {num})"
                else:
                    expr += f" {op} {num}"
                current = ops[op](current, num)
                if current is None:
                    break
            if abs(current - n) < 0.0001:  # 允许浮点误差
                return expr
        except:
            continue
    
    # 尝试阶乘组合
    if n <= 20:  # 20以内的数可以用阶乘表示
        fact = math.factorial(114514)  # 虽然这个值极大，但可以通过对数操作简化
        return f"log({fact}) / log({n})" if n > 1 else f"{fact} / {fact}"
    
    return None

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        try:
            target = int(sys.argv[1])
            result = find_combination(target)
            if result:
                print(f"{target} = {result}")
            else:
                print("未能找到合适的114514组合式，可以尝试：")
                print("1. 增加更多114514的使用数量")
                print("2. 结合阶乘、平方根等高级运算")
                print("3. 使用多个表达式组合计算")
        except ValueError:
            print("请输入有效的整数")
    else:
        print("使用方法：python number_generator.py [目标数字]")
        print("示例：")
        print("python number_generator.py 1  => 114514 / 114514")
        print("python number_generator.py 3  => (114514 + 114514 + 114514) / 114514")