## Common types
string_val: str = 'This is demo'
int_val: int = 10
bool_val: bool = True
float_val: float = 101.11

## List type
names: list[str] = ["Test1", "Test2", "Test3"]

## Typing function parameters
def test_fun(arg1: str,  arg2: str) -> str:
    return arg1 + arg2
res = test_fun("string 1", "string 2")
# print(res)

