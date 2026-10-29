import pytest

from python_linq import (
    Enumerable,
    TakeEnumerableException,
    TakeEnumerableExceptionCase,
)


class TestAggregateEnumerable:
    """Tests for AggregateEnumerable methods via enumerable API"""

    def test_scan_with_seed(self):
        """Test scan with seed parameter"""
        data = [1, 2, 3, 4]
        results = Enumerable(data).scan(lambda acc, x: acc + x, seed=0)

        assert list(results) == [0, 1, 3, 6, 10]

    def test_scan_without_seed(self):
        """Test scan without seed (uses first element as initial accumulator)"""
        data = [1, 2, 3, 4]
        results = Enumerable(data).scan(lambda acc, x: acc + x)

        assert list(results) == [1, 3, 6, 10]

    def test_fold(self):
        """Test that fold is available via enumerable API"""
        data = [1, 2, 3]
        result = Enumerable(data).fold(lambda acc, x: acc + x)

        assert result == 6

    def test_scan_equals_itertools_accumulate_without_initial(self):
        """Test scan matches itertools.accumulate behavior without initial"""
        from itertools import accumulate

        data = [1, 2, 3, 4]
        results = list(Enumerable(data).scan(lambda acc, x: acc + x))
        expected = list(accumulate(data))

        assert results == expected

    def test_scan_with_initial_matches_itertools(self):
        """Test scan with seed matches itertools.accumulate with initial"""
        from itertools import accumulate

        data = [1, 2, 3, 4]
        results = list(Enumerable(data).scan(lambda acc, x: acc + x, seed=0))
        expected = list(accumulate(data, initial=0))

        assert results == expected

    def test_scan_multiplication_accumulator(self):
        """Test scan with multiplication accumulator"""
        data = [1, 2, 3, 4]
        results = Enumerable(data).scan(lambda acc, x: acc * x)

        assert list(results) == [1, 2, 6, 24]

    def test_fold_multiplication(self):
        """Test fold with multiplication"""
        data = [1, 2, 3, 4]
        result = Enumerable(data).fold(lambda acc, x: acc * x)

        assert result == 24

    def test_scan_first_element_as_seed(self):
        """Test scan when using first element as initial value"""
        data = ["a", "b", "c"]
        results = Enumerable(data).scan(lambda acc, x: acc + x)

        assert list(results) == ["a", "ab", "abc"]

    def test_scan_empty_enumerable_with_seed(self):
        """Test scan on empty enumerable with seed"""
        data: list[int] = []
        results = Enumerable(data).scan(lambda acc, x: acc + x, seed=0)

        assert list(results) == [0]

    def test_scan_without_seed_fails_on_empty(self):
        """Test scan on empty enumerable without seed raises TakeEnumerableException when iterated"""
        # When calling .scan() on empty enumerable without seed, it creates a generator that will
        # try to call self.first() immediately within the generator function.
        # However, due to lazy evaluation, this happens during iteration, not at creation time.
        results = Enumerable[int]([]).scan(lambda acc, x: acc + x)
        # The exception should be raised when we try to consume the generator
        with pytest.raises(TakeEnumerableException) as exc:
            results.to_list()
        assert exc.value.exception_case == TakeEnumerableExceptionCase.NotEnoughItems

    def test_fold_with_seed(self):
        """Test fold with seed parameter"""
        data = [1, 2, 3]
        result = Enumerable(data).fold(lambda acc, x: acc + x, seed=0)

        assert result == 6

    def test_fold_without_seed(self):
        """Test fold without seed (uses first element as initial value)"""
        data = [1, 2, 3]
        result = Enumerable(data).fold(lambda acc, x: acc + x)

        assert result == 6

    def test_fold_single_element_with_seed(self):
        """Test fold on single element with seed"""
        data = [5]
        result = Enumerable(data).fold(lambda acc, x: acc + x, seed=0)

        assert result == 5

    def test_fold_empty_enumerable_with_seed(self):
        """Test fold on empty enumerable with seed"""
        data: list[int] = []
        result = Enumerable(data).fold(lambda acc, x: acc + x, seed=100)

        assert result == 100

    def test_fold_empty_enumerable_without_seed(self):
        """Test fold on empty enumerable without seed raises TakeEnumerableException"""
        with pytest.raises(TakeEnumerableException) as exc:
            Enumerable[int]([]).fold(lambda acc, x: acc + x)
        assert exc.value.exception_case == TakeEnumerableExceptionCase.NotEnoughItems

    def test_scan_with_seed_only_yields_seed(self):
        """Test scan on empty enumerable with seed yields just the seed"""
        results = Enumerable[int]([]).scan(lambda acc, x: acc + x, seed=42)
        assert list(results) == [42]

    def test_join_with_default_aggregator(self):
        """Test join with default string concatenation aggregator"""
        data = ["a", "b"]
        result = Enumerable(data).join(" ")

        assert result == "a b"

    def test_join_with_custom_aggregator(self):
        """Test join with custom string aggregator"""
        data = ["a", "b"]
        result = Enumerable(data).join("", lambda x, y: f"{x}{y}")

        assert result == "ab"

    def test_join_multiple_elements_text(self):
        """Test join on multiple elements with comma separator"""
        data = ["1", "2", "3"]
        result = Enumerable(data).join(", ")

        assert result == "1, 2, 3"

    def test_scan_with_mixed_types(self):
        """Test scan with mixed type operations"""
        # Scan yields the initial seed value plus every intermediate accumulation state
        data: list[int | str] = [1, "a", 2]
        results = Enumerable(data).scan(lambda acc, x: f"{acc}={x}", seed="")

        # Expected: initial "", then after each element processing
        assert list(results) == ["", "=1", "=1=a", "=1=a=2"]

    def test_fold_and_returns_value(self):
        """Test that fold returns the final aggregated value"""
        # Starting with seed=True, processing [True, False] with `acc and x` logic:
        # - Initial: acc = True (seed)
        # - After True: acc = True and True = True
        # - After False: acc = True and False = False
        data = [True, False]
        result = Enumerable(data).fold(lambda acc, x: acc and x, seed=True)

        assert isinstance(result, bool)
        assert result == False  # (True and True) and False = False

    def test_scan_without_seed_uses_first_element(self):
        """Test scan without seed uses first element as initial value"""
        data = [10, 20, 30]
        results = Enumerable(data).scan(lambda acc, x: acc + x)

        assert list(results) == [10, 30, 60]

    def test_fold_without_seed_raises_on_empty(self):
        """Test fold on empty enumerable without seed raises TakeEnumerableException"""
        with pytest.raises(TakeEnumerableException) as exc:
            Enumerable[int]([]).fold(lambda acc, x: acc + x)
        assert exc.value.exception_case == TakeEnumerableExceptionCase.NotEnoughItems
