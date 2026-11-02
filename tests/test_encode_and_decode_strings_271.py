import pytest

from encode_and_decode_strings_271 import Solution


@pytest.mark.parametrize(
    "strs",
    [
        (["hello,world", "hello"]),
        (["Hello", "World"]),
        ([""]),
        (["abc#def", "", "hello"]),
        [],
    ],
)
def test_encode_and_decode_strings_271(strs: list[str]):
    solution = Solution()
    encoded = solution.encode(strs)
    result = solution.decode(encoded)
    assert result == strs
