import codewars_test as test
import kata as Kata

get_count = Kata.get_count


@test.describe("Get Count Vowel")
def sample_tests():

    @test.it("Should count all vowels")
    def all_vowels():
        test.assert_equals(get_count("aeiou"), 5,
                           f"Incorrect answer for \"aeiou\"")

    @test.it("Should not count \"y\"")
    def only_y():
        test.assert_equals(get_count("y"), 0,
                           f"Incorrect answer for \"y\"")

    @test.it("Should return 0 when no vowels")
    def no_vowels():
        test.assert_equals(get_count("bcdfghjklmnpqrstvwxz y"),
                           0, f"Incorrect answer for \"bcdfghjklmnpqrstvwxz y\"")

    @test.it("Should return 0 for empty string")
    def no_vowels():
        test.assert_equals(
            get_count(""), 0, f"Incorrect answer for empty string")

    @test.it("Should return 5 for \"abracadabra\"")
    def test_abracadabra():
        test.assert_equals(get_count("abracadabra"), 5,
                           f"Incorrect answer for \"abracadabra\"")
