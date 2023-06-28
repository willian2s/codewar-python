import codewars_test as test
import kata as kata

duplicate_encode = kata.duplicate_encode


@test.describe("Duplicate Encoder")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(duplicate_encode("din"), "(((")
        test.assert_equals(duplicate_encode("recede"), "()()()")
        test.assert_equals(duplicate_encode("Success"),
                           ")())())", "should ignore case")
        test.assert_equals(duplicate_encode("(( @"), "))((")
