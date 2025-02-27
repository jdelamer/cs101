class Country:
    """
    Class for keeping track of country details for the purpose of the Country Catalogue's functionality. Country objects
    know their name, which continent they are on, their population, and their surface area.
    """

    def __init__(self, name: str, continent: str, population: int, area: float):


    def population_density(self) -> float:
        """
        Calculate and return the population density of the Country. Population density is calculated with
        population/area.

        :return: The population density of the Country.
        :rtype: float.
        """


    def __eq__(self, other: "Country") -> bool:
        """
        Check if two instances of a Country object are equal. Country objects are considered equal if all attributes are
        equal.

        :param other: A Country object to compare the self Country to.
        :type other: Country.
        :return: True if the Country objects have all attributes equal.
        :rtype: boolean.
        """


    def __repr__(self) -> str:
        """
        Returns a string representation of the Country object. The string is "name, continent, population, area".

        :return: String representation of the Country object of the form "name, continent, population, area".
        :rtype: String.
        """

import unittest

class CountryTest(unittest.TestCase):
    def test_country_name_returns_correct_country_name(self):
        country = Country("Name", "Continent", 123456789, 987654321)
        self.assertEqual("Name", country.name)

    def test_country_continent_returns_correct_country_continent(self):
        country = Country("Name", "Continent", 123456789, 987654321)
        self.assertEqual("Continent", country.continent)

    def test_country_population_returns_correct_country_population(self):
        country = Country("Name", "Continent", 123456789, 987654321)
        self.assertEqual(123456789, country.population)

    def test_country_area_returns_correct_country_area(self):
        country = Country("Name", "Continent", 123456789, 987654321)
        self.assertEqual(987654321, country.area)

    def test_population_density_returns_correct_population_density(self):
        country = Country("Name", "Continent", 123456789, 987654321)
        self.assertAlmostEqual(123456789 / 987654321, country.population_density())

    def test_population_density_with_zero_area_raises_zero_division_error(self):
        country = Country("Name", "Continent", 123456789, 0)
        with self.assertRaises(ZeroDivisionError):
            country.population_density()

    def test_equals_equal_country_objects_returns_true(self):
        country_a = Country("Name", "Continent", 123456789, 987654321)
        country_b = Country("Name", "Continent", 123456789, 987654321)
        self.assertEqual(country_a, country_b)

    def test_equals_unequal_country_objects_returns_false(self):
        country = Country("Name", "Continent", 123456789, 987654321)
        cases = [
            Country("Eman", "Continent", 123456789, 987654321),
            Country("Name", "Tnenitnoc", 123456789, 987654321),
            Country("Name", "Continent", 987654321, 987654321),
            Country("Name", "Continent", 123456789, 123456789),
            Country("Eman", "Tnenitnoc", 987654321, 123456789),
            54321,
        ]
        for case in cases:
            with self.subTest(case=case):
                self.assertNotEqual(country, case)

    def test_repr_arbitrary_country_returns_correct_string(self):
        country = Country("Name", "Continent", 123456789, 987654321)
        self.assertEqual("Country(name=Name, continent=Continent, population=123456789, area=987654321)", str(country))

class CountryCatalogue:
    """
    Class for managing a collection of Country Objects. The class maintains a list of the Country objects and provides
    a mechanism for adding, removing, finding, checking if exists, and other collection-ie type methods.
    """

    def __init__(self):


    def _find(self, country: Country) -> int:
        """
        Find the index of the specified Country within the Country Catalogue. If the Country does not exist, return the
        sentinel value of -1.

        :param country: Country object to search for.
        :type country: Country object.
        :return: Index of the Country with the matching values.
        :rtype: integer.
        """


    def contains(self, country: Country) -> bool:
        """
        Check if a Country with the provided values exists within the collection. Returns True if it does and False
        otherwise.

        :param country: Country object to search for.
        :type country: Country object.
        :return: True if the Country object is contained within the CountryCatalogue, False otherwise.
        :rtype: bool.
        """


    def add(self, country: Country) -> None:
        """
        Add the provided Country object to the Country Catalogue.

        :param country: Country object to add to the collection.
        :type country: Country object.
        :param area: Area of the country.
        :type area: float.
        """


    def remove(self, country: Country) -> Country:
        """
        Remove a Country object from the Country Catalogue matching the provided value. The removed Country object is
        returned by the method. If no such Country object exists within the collection, a ValueError is raised.

        :raise ValueError: If the Country object does not exist within the collection, a ValueError is raised.
        :param country: Country object to remove from the collection.
        :type country: Country object.
        """


    def country_with_largest_population_density(self) -> Country:
        """
        Find and return the Country object with the largest population density. A reference to the Country object with
        the largest density is returned. If the collection is empty, a IndexError is raised.

        :raise IndexError: If the collection is empty, raise an IndexError.
        :return: Country object with the largest population density.
        :rtype: Country.
        """


    def country_with_smallest_population_density(self) -> Country:
        """
        Find and return the Country object with the smallest population density. A reference to the Country object with
        the smallest density is returned. If the collection is empty, a IndexError is raised.

        :raise IndexError: If the collection is empty, raise an IndexError.
        :return: Country object with the smallest population density.
        :rtype: Country.
        """


    def filter_countries_by_population_density(self, low_limit: float, high_limit: float) -> "CountryCatalogue":
        """
        Return a new CountryCatalogue containing only Country objects from the current CountryCatalogue with a
        population density between the specified low & high range. If no Country objects between the specified range
        exist, an empty CountryCatalogue is returned.

        :param low_limit: The low population density; only Country objects with a population density greater than or
        equal to the low_limit will be included in the filtered CountryCatalogue.
        :type low_limit: float
        :param high_limit: The high population density; only Country objects with a population density strictly less
        than the high_limit will be included in the filtered CountryCatalogue.
        :type high_limit: float
        :return: A new CountryCatalogue object with copies of Country objects that fall within the specified range.
        :rtype: CountryCatalogue
        """


    def most_populous_continent(self) -> str:
        """
        Find and return the name of the continent with the largest population based on the Country objects within the
        CountryCatalogue. If two or more continents have the same largest population, return the name of the country
        found first. If the collection is empty, a IndexError is raised.

        :raise IndexError: If the collection is empty, raise an IndexError.
        :return: Name of the continent with the largest population.
        :rtype: str.
        """


    def __getitem__(self, item: int) -> Country:


    def __len__(self) -> int:


    def __eq__(self, other: "CountryCatalogue") -> bool:


    def __repr__(self) -> str:

import unittest

class CountryCatalogueTest(unittest.TestCase):
    def test_len_empty_collection_returns_0(self):
        empty_country_catalogue = CountryCatalogue()
        self.assertEqual(0, len(empty_country_catalogue))

    def test_contains_empty_collection_returns_false(self):
        empty_country_catalogue = CountryCatalogue()
        self.assertFalse(empty_country_catalogue.contains(Country("Name", "Continent", 123456789, 987654321)))

    def test_remove_empty_collection_raises_value_error(self):
        empty_country_catalogue = CountryCatalogue()
        with self.assertRaises(ValueError):
            empty_country_catalogue.remove(Country("Name", "Continent", 123456789, 987654321))

    def test_country_with_largest_population_density_empty_collection_raises_index_error(self):
        empty_country_catalogue = CountryCatalogue()
        with self.assertRaises(IndexError):
            empty_country_catalogue.country_with_largest_population_density()

    def test_country_with_smallest_population_density_empty_collection_raises_index_error(self):
        empty_country_catalogue = CountryCatalogue()
        with self.assertRaises(IndexError):
            empty_country_catalogue.country_with_smallest_population_density()

    def test_filter_countries_by_population_density_empty_collection_returns_empty_country_catalogue(self):
        empty_country_catalogue = CountryCatalogue()
        self.assertEqual(CountryCatalogue(), empty_country_catalogue.filter_countries_by_population_density(0, 10000))

    def test_most_populous_continent_empty_collection_raises_index_error(self):
        empty_country_catalogue = CountryCatalogue()
        with self.assertRaises(IndexError):
            empty_country_catalogue.most_populous_continent()

    def test_getitem_empty_collection_raises_index_error(self):
        empty_country_catalogue = CountryCatalogue()
        indicies = [-1, 0, 1]
        for index in indicies:
            with self.subTest(index=index):
                with self.assertRaises(IndexError):
                    empty_country_catalogue[index]

    def test_repr_empty_collection_returns_empty_string(self):
        empty_country_catalogue = CountryCatalogue()
        self.assertEqual("", str(empty_country_catalogue))

    def test_len_singleton_returns_1(self):
        singleton_country_catalogue = CountryCatalogue()
        singleton_country_catalogue.add(Country("Name", "Continent", 123456789, 987654321))
        self.assertEqual(1, len(singleton_country_catalogue))

    def test_contains_singleton_country_exists_returns_true(self):
        singleton_country_catalogue = CountryCatalogue()
        singleton_country_catalogue.add(Country("Name", "Continent", 123456789, 987654321))
        self.assertTrue(singleton_country_catalogue.contains(Country("Name", "Continent", 123456789, 987654321)))

    def test_contains_singleton_country_not_exists_returns_false(self):
        singleton_country_catalogue = CountryCatalogue()
        singleton_country_catalogue.add(Country("Name", "Continent", 123456789, 987654321))
        self.assertFalse(singleton_country_catalogue.contains(Country("Eman", "Tnenitnoc", 987654321, 123456789)))

    def test_remove_singleton_country_exists_returns_country(self):
        singleton_country_catalogue = CountryCatalogue()
        singleton_country_catalogue.add(Country("Name", "Continent", 123456789, 987654321))
        self.assertEqual(
            Country("Name", "Continent", 123456789, 987654321),
            singleton_country_catalogue.remove(Country("Name", "Continent", 123456789, 987654321)),
        )

    def test_remove_singleton_country_exists_removes_country(self):
        singleton_country_catalogue = CountryCatalogue()
        singleton_country_catalogue.add(Country("Name", "Continent", 123456789, 987654321))
        singleton_country_catalogue.remove(Country("Name", "Continent", 123456789, 987654321))
        self.assertFalse(singleton_country_catalogue.contains(Country("Name", "Continent", 123456789, 987654321)))

    def test_remove_singleton_country_not_exists_raises_value_error(self):
        singleton_country_catalogue = CountryCatalogue()
        singleton_country_catalogue.add(Country("Name", "Continent", 123456789, 987654321))
        with self.assertRaises(ValueError):
            singleton_country_catalogue.remove(Country("Eman", "Tnenitnoc", 987654321, 123456789))

    def test_country_with_largest_population_density_singleton_returns_correct_country(self):
        singleton_country_catalogue = CountryCatalogue()
        singleton_country_catalogue.add(Country("Name", "Continent", 123456789, 987654321))
        self.assertEqual(
            Country("Name", "Continent", 123456789, 987654321),
            singleton_country_catalogue.country_with_largest_population_density(),
        )

    def test_country_with_smallest_population_density_singleton_returns_correct_country(self):
        singleton_country_catalogue = CountryCatalogue()
        singleton_country_catalogue.add(Country("Name", "Continent", 123456789, 987654321))
        self.assertEqual(
            Country("Name", "Continent", 123456789, 987654321),
            singleton_country_catalogue.country_with_smallest_population_density(),
        )

    def test_filter_countries_by_population_density_singleton_not_within_range_returns_empty_country_catalogue(self):
        singleton_country_catalogue = CountryCatalogue()
        singleton_country_catalogue.add(Country("Name", "Continent", 10, 1))
        self.assertEqual(CountryCatalogue(), singleton_country_catalogue.filter_countries_by_population_density(0, 5))

    def test_filter_countries_by_population_density_singleton_within_range_returns_correct_country_catalogue(self):
        singleton_country_catalogue = CountryCatalogue()
        singleton_country_catalogue.add(Country("Name", "Continent", 10, 1))
        expected_country_catalogue = CountryCatalogue()
        expected_country_catalogue.add(Country("Name", "Continent", 10, 1))
        filtered_country_catalogue = singleton_country_catalogue.filter_countries_by_population_density(0, 100)
        self.assertEqual(expected_country_catalogue, filtered_country_catalogue)

    def test_filter_countries_by_population_density_singleton_equal_low_limit_returns_correct_country_catalogue(self):
        singleton_country_catalogue = CountryCatalogue()
        singleton_country_catalogue.add(Country("Name", "Continent", 10, 1))
        expected_country_catalogue = CountryCatalogue()
        expected_country_catalogue.add(Country("Name", "Continent", 10, 1))
        filtered_country_catalogue = singleton_country_catalogue.filter_countries_by_population_density(10, 100)
        self.assertEqual(expected_country_catalogue, filtered_country_catalogue)

    def test_filter_countries_by_population_density_singleton_equal_high_limit_returns_empty_country_catalogue(
        self,
    ):
        singleton_country_catalogue = CountryCatalogue()
        singleton_country_catalogue.add(Country("Name", "Continent", 10, 1))
        filtered_country_catalogue = singleton_country_catalogue.filter_countries_by_population_density(0, 10)
        self.assertEqual(CountryCatalogue(), filtered_country_catalogue)

    def test_filter_countries_by_population_density_singleton_low_high_high_low_returns_empty_country_catalogue(
        self,
    ):
        singleton_country_catalogue = CountryCatalogue()
        singleton_country_catalogue.add(Country("Name", "Continent", 10, 1))
        filtered_country_catalogue = singleton_country_catalogue.filter_countries_by_population_density(100, 0)
        self.assertEqual(CountryCatalogue(), filtered_country_catalogue)

    def test_most_populous_continent_singleton_returns_correct_continent(self):
        singleton_country_catalogue = CountryCatalogue()
        singleton_country_catalogue.add(Country("Name", "Continent", 10, 1))
        self.assertEqual("Continent", singleton_country_catalogue.most_populous_continent())

    def test_getitem_valid_index_singleton_returns_item(self):
        singleton_country_catalogue = CountryCatalogue()
        singleton_country_catalogue.add(Country("Name", "Continent", 123456789, 987654321))
        self.assertEqual(Country("Name", "Continent", 123456789, 987654321), singleton_country_catalogue[0])

    def test_getitem_invalid_index_singleton_raises_index_error(self):
        singleton_country_catalogue = CountryCatalogue()
        singleton_country_catalogue.add(Country("Name", "Continent", 123456789, 987654321))
        with self.assertRaises(IndexError):
            singleton_country_catalogue[1]

    def test_repr_singleton_returns_correct_string(self):
        singleton_country_catalogue = CountryCatalogue()
        singleton_country_catalogue.add(Country("Name", "Continent", 123456789, 987654321))
        self.assertEqual(
            "Country(name=Name, continent=Continent, population=123456789, area=987654321)\n",
            str(singleton_country_catalogue),
        )

    def test_len_many_returns_correct_length(self):
        many_country_catalogue = CountryCatalogue()
        many_country_catalogue.add(Country("Name_1", "Continent_1", 123456789, 987654321))
        many_country_catalogue.add(Country("Name_2", "Continent_2", 123456789, 987654321))
        many_country_catalogue.add(Country("Name_3", "Continent_3", 123456789, 987654321))
        many_country_catalogue.add(Country("Name_4", "Continent_4", 123456789, 987654321))
        many_country_catalogue.add(Country("Name_5", "Continent_5", 123456789, 987654321))
        self.assertEqual(5, len(many_country_catalogue))

    def test_contains_many_country_exists_returns_true(self):
        many_country_catalogue = CountryCatalogue()
        many_country_catalogue.add(Country("Name_1", "Continent_1", 123456789, 987654321))
        many_country_catalogue.add(Country("Name_2", "Continent_2", 123456789, 987654321))
        many_country_catalogue.add(Country("Name_3", "Continent_3", 123456789, 987654321))
        many_country_catalogue.add(Country("Name_4", "Continent_4", 123456789, 987654321))
        many_country_catalogue.add(Country("Name_5", "Continent_5", 123456789, 987654321))
        self.assertTrue(many_country_catalogue.contains(Country("Name_3", "Continent_3", 123456789, 987654321)))

    def test_contains_many_country_not_exists_returns_false(self):
        many_country_catalogue = CountryCatalogue()
        many_country_catalogue.add(Country("Name_1", "Continent_1", 123456789, 987654321))
        many_country_catalogue.add(Country("Name_2", "Continent_2", 123456789, 987654321))
        many_country_catalogue.add(Country("Name_3", "Continent_3", 123456789, 987654321))
        many_country_catalogue.add(Country("Name_4", "Continent_4", 123456789, 987654321))
        many_country_catalogue.add(Country("Name_5", "Continent_5", 123456789, 987654321))
        self.assertFalse(many_country_catalogue.contains(Country("Eman", "Tnenitnoc", 987654321, 123456789)))

    def test_remove_many_country_exists_returns_country(self):
        many_country_catalogue = CountryCatalogue()
        many_country_catalogue.add(Country("Name_1", "Continent_1", 123456789, 987654321))
        many_country_catalogue.add(Country("Name_2", "Continent_2", 123456789, 987654321))
        many_country_catalogue.add(Country("Name_3", "Continent_3", 123456789, 987654321))
        many_country_catalogue.add(Country("Name_4", "Continent_4", 123456789, 987654321))
        many_country_catalogue.add(Country("Name_5", "Continent_5", 123456789, 987654321))
        country = Country("Name_3", "Continent_3", 123456789, 987654321)
        self.assertEqual(country, many_country_catalogue.remove(Country("Name_3", "Continent_3", 123456789, 987654321)))

    def test_remove_many_country_exists_removes_country(self):
        many_country_catalogue = CountryCatalogue()
        many_country_catalogue.add(Country("Name_1", "Continent_1", 123456789, 987654321))
        many_country_catalogue.add(Country("Name_2", "Continent_2", 123456789, 987654321))
        many_country_catalogue.add(Country("Name_3", "Continent_3", 123456789, 987654321))
        many_country_catalogue.add(Country("Name_4", "Continent_4", 123456789, 987654321))
        many_country_catalogue.add(Country("Name_5", "Continent_5", 123456789, 987654321))
        many_country_catalogue.remove(Country("Name_3", "Continent_3", 123456789, 987654321))
        self.assertFalse(many_country_catalogue.contains(Country("Name_3", "Continent_3", 123456789, 987654321)))

    def test_remove_many_country_not_exists_raises_value_error(self):
        many_country_catalogue = CountryCatalogue()
        many_country_catalogue.add(Country("Name_1", "Continent_1", 123456789, 987654321))
        many_country_catalogue.add(Country("Name_2", "Continent_2", 123456789, 987654321))
        many_country_catalogue.add(Country("Name_3", "Continent_3", 123456789, 987654321))
        many_country_catalogue.add(Country("Name_4", "Continent_4", 123456789, 987654321))
        many_country_catalogue.add(Country("Name_5", "Continent_5", 123456789, 987654321))
        with self.assertRaises(ValueError):
            many_country_catalogue.remove(Country("Eman", "Tnenitnoc", 987654321, 123456789))

    def test_country_with_largest_population_density_many_returns_correct_country(self):
        many_country_catalogue = CountryCatalogue()
        many_country_catalogue.add(Country("Name_1", "Continent_1", 5, 1))
        many_country_catalogue.add(Country("Name_2", "Continent_2", 2, 1))
        many_country_catalogue.add(Country("Name_3", "Continent_3", 10, 1))
        many_country_catalogue.add(Country("Name_4", "Continent_4", 6, 1))
        many_country_catalogue.add(Country("Name_5", "Continent_5", 1, 1))
        self.assertEqual(
            Country("Name_3", "Continent_3", 10, 1), many_country_catalogue.country_with_largest_population_density()
        )

    def test_country_with_smallest_population_density_many_returns_correct_country(self):
        many_country_catalogue = CountryCatalogue()
        many_country_catalogue.add(Country("Name_1", "Continent_1", 5, 1))
        many_country_catalogue.add(Country("Name_2", "Continent_2", 2, 1))
        many_country_catalogue.add(Country("Name_3", "Continent_3", 10, 1))
        many_country_catalogue.add(Country("Name_4", "Continent_4", 6, 1))
        many_country_catalogue.add(Country("Name_5", "Continent_5", 1, 1))
        self.assertEqual(
            Country("Name_5", "Continent_5", 1, 1), many_country_catalogue.country_with_smallest_population_density()
        )

    def test_filter_countries_by_population_density_many_not_within_range_returns_empty_country_catalogue(self):
        many_country_catalogue = CountryCatalogue()
        many_country_catalogue.add(Country("Name_1", "Continent_1", 5, 1))
        many_country_catalogue.add(Country("Name_2", "Continent_2", 2, 1))
        many_country_catalogue.add(Country("Name_3", "Continent_3", 10, 1))
        many_country_catalogue.add(Country("Name_4", "Continent_4", 6, 1))
        many_country_catalogue.add(Country("Name_5", "Continent_5", 1, 1))
        self.assertEqual(CountryCatalogue(), many_country_catalogue.filter_countries_by_population_density(50, 100))

    def test_filter_countries_by_population_density_many_within_range_returns_correct_country_catalog(self):
        many_country_catalogue = CountryCatalogue()
        many_country_catalogue.add(Country("Name_1", "Continent_1", 5, 1))
        many_country_catalogue.add(Country("Name_2", "Continent_2", 2, 1))
        many_country_catalogue.add(Country("Name_3", "Continent_3", 10, 1))
        many_country_catalogue.add(Country("Name_4", "Continent_4", 6, 1))
        many_country_catalogue.add(Country("Name_5", "Continent_5", 1, 1))
        expected = CountryCatalogue()
        expected.add(Country("Name_1", "Continent_1", 5, 1))
        expected.add(Country("Name_2", "Continent_2", 2, 1))
        expected.add(Country("Name_4", "Continent_4", 6, 1))
        expected.add(Country("Name_5", "Continent_5", 1, 1))
        filtered_country_catalogue = many_country_catalogue.filter_countries_by_population_density(0, 10)
        self.assertEqual(expected, filtered_country_catalogue)

    def test_filter_countries_by_population_density_many_equal_low_limit_returns_correct_country_catalogue(self):
        many_country_catalogue = CountryCatalogue()
        many_country_catalogue.add(Country("Name_1", "Continent_1", 5, 1))
        many_country_catalogue.add(Country("Name_2", "Continent_2", 2, 1))
        many_country_catalogue.add(Country("Name_3", "Continent_3", 10, 1))
        many_country_catalogue.add(Country("Name_4", "Continent_4", 6, 1))
        many_country_catalogue.add(Country("Name_5", "Continent_5", 1, 1))
        expected = CountryCatalogue()
        expected.add(Country("Name_3", "Continent_3", 10, 1))
        filtered_country_catalogue = many_country_catalogue.filter_countries_by_population_density(10, 100)
        self.assertEqual(expected, filtered_country_catalogue)

    def test_filter_countries_by_population_density_many_equal_high_limit_returns_empty_country_catalogue(
        self,
    ):
        many_country_catalogue = CountryCatalogue()
        many_country_catalogue.add(Country("Name_1", "Continent_1", 5, 1))
        many_country_catalogue.add(Country("Name_2", "Continent_2", 2, 1))
        many_country_catalogue.add(Country("Name_3", "Continent_3", 10, 1))
        many_country_catalogue.add(Country("Name_4", "Continent_4", 6, 1))
        many_country_catalogue.add(Country("Name_5", "Continent_5", 1, 1))
        filtered_country_catalogue = many_country_catalogue.filter_countries_by_population_density(0, 1)
        self.assertEqual(CountryCatalogue(), filtered_country_catalogue)

    def test_filter_countries_by_population_density_many_low_high_high_low_returns_empty_country_catalogue(
        self,
    ):
        many_country_catalogue = CountryCatalogue()
        many_country_catalogue.add(Country("Name_1", "Continent_1", 5, 1))
        many_country_catalogue.add(Country("Name_2", "Continent_2", 2, 1))
        many_country_catalogue.add(Country("Name_3", "Continent_3", 10, 1))
        many_country_catalogue.add(Country("Name_4", "Continent_4", 6, 1))
        many_country_catalogue.add(Country("Name_5", "Continent_5", 1, 1))
        filtered_country_catalogue = many_country_catalogue.filter_countries_by_population_density(100, 0)
        self.assertEqual(CountryCatalogue(), filtered_country_catalogue)

    def test_most_populous_continent_many_returns_correct_continent(self):
        many_country_catalogue = CountryCatalogue()
        many_country_catalogue.add(Country("Name_1", "Continent_1", 5, 1))
        many_country_catalogue.add(Country("Name_2", "Continent_1", 2, 1))
        many_country_catalogue.add(Country("Name_3", "Continent_2", 10, 1))
        many_country_catalogue.add(Country("Name_4", "Continent_2", 6, 1))
        many_country_catalogue.add(Country("Name_5", "Continent_3", 1, 1))
        self.assertEqual("Continent_2", many_country_catalogue.most_populous_continent())

    def test_getitem_valid_index_many_returns_item(self):
        many_country_catalogue = CountryCatalogue()
        countries = []
        countries.append(Country("Name_1", "Continent_1", 123456789, 987654321))
        countries.append(Country("Name_2", "Continent_2", 123456789, 987654321))
        countries.append(Country("Name_3", "Continent_3", 123456789, 987654321))
        countries.append(Country("Name_4", "Continent_4", 123456789, 987654321))
        countries.append(Country("Name_5", "Continent_5", 123456789, 987654321))
        many_country_catalogue.add(Country("Name_1", "Continent_1", 123456789, 987654321))
        many_country_catalogue.add(Country("Name_2", "Continent_2", 123456789, 987654321))
        many_country_catalogue.add(Country("Name_3", "Continent_3", 123456789, 987654321))
        many_country_catalogue.add(Country("Name_4", "Continent_4", 123456789, 987654321))
        many_country_catalogue.add(Country("Name_5", "Continent_5", 123456789, 987654321))
        for index, country in enumerate(countries):
            with self.subTest(index=index, country=country):
                self.assertEqual(country, many_country_catalogue[index])

    def test_getitem_invalid_index_many_raises_index_error(self):
        many_country_catalogue = CountryCatalogue()
        many_country_catalogue.add(Country("Name_1", "Continent_1", 123456789, 987654321))
        many_country_catalogue.add(Country("Name_2", "Continent_2", 123456789, 987654321))
        many_country_catalogue.add(Country("Name_3", "Continent_3", 123456789, 987654321))
        many_country_catalogue.add(Country("Name_4", "Continent_4", 123456789, 987654321))
        many_country_catalogue.add(Country("Name_5", "Continent_5", 123456789, 987654321))
        with self.assertRaises(IndexError):
            many_country_catalogue[5]

    def test_repr_many_returns_correct_string(self):
        many_country_catalogue = CountryCatalogue()
        many_country_catalogue.add(Country("Name_1", "Continent_1", 123456789, 987654321))
        many_country_catalogue.add(Country("Name_2", "Continent_2", 123456789, 987654321))
        many_country_catalogue.add(Country("Name_3", "Continent_3", 123456789, 987654321))
        many_country_catalogue.add(Country("Name_4", "Continent_4", 123456789, 987654321))
        many_country_catalogue.add(Country("Name_5", "Continent_5", 123456789, 987654321))
        expected = (
            "Country(name=Name_1, continent=Continent_1, population=123456789, area=987654321)\n"
            "Country(name=Name_2, continent=Continent_2, population=123456789, area=987654321)\n"
            "Country(name=Name_3, continent=Continent_3, population=123456789, area=987654321)\n"
            "Country(name=Name_4, continent=Continent_4, population=123456789, area=987654321)\n"
            "Country(name=Name_5, continent=Continent_5, population=123456789, area=987654321)\n"
        )
        self.assertEqual(expected, str(many_country_catalogue))

    def test_remove_two_duplicate_country_exists_leaves_one_duplicate(self):
        duplicate_country_catalogue = CountryCatalogue()
        duplicate_country_catalogue.add(Country("Name_1", "Continent_1", 123456789, 987654321))
        duplicate_country_catalogue.add(Country("Name_2", "Continent_2", 123456789, 987654321))
        duplicate_country_catalogue.add(Country("Name_2", "Continent_2", 123456789, 987654321))
        duplicate_country_catalogue.add(Country("Name_4", "Continent_4", 123456789, 987654321))
        duplicate_country_catalogue.add(Country("Name_5", "Continent_5", 123456789, 987654321))
        duplicate_country_catalogue.remove(Country("Name_2", "Continent_2", 123456789, 987654321))
        self.assertTrue(duplicate_country_catalogue.contains(Country("Name_2", "Continent_2", 123456789, 987654321)))

    def test_remove_two_duplicate_country_exists_two_remove_calls_removes_both_duplicates(self):
        duplicate_country_catalogue = CountryCatalogue()
        duplicate_country_catalogue.add(Country("Name_1", "Continent_1", 123456789, 987654321))
        duplicate_country_catalogue.add(Country("Name_2", "Continent_2", 123456789, 987654321))
        duplicate_country_catalogue.add(Country("Name_2", "Continent_2", 123456789, 987654321))
        duplicate_country_catalogue.add(Country("Name_4", "Continent_4", 123456789, 987654321))
        duplicate_country_catalogue.add(Country("Name_5", "Continent_5", 123456789, 987654321))
        duplicate_country_catalogue.remove(Country("Name_2", "Continent_2", 123456789, 987654321))
        duplicate_country_catalogue.remove(Country("Name_2", "Continent_2", 123456789, 987654321))
        self.assertFalse(duplicate_country_catalogue.contains(Country("Name_2", "Continent_2", 123456789, 987654321)))

    def test_country_with_largest_population_density_duplicate_densities_returns_correct_country(self):
        many_country_catalogue = CountryCatalogue()
        many_country_catalogue.add(Country("Name_1", "Continent_1", 5, 1))
        many_country_catalogue.add(Country("Name_2", "Continent_2", 2, 1))
        many_country_catalogue.add(Country("Name_3", "Continent_3", 10, 1))
        many_country_catalogue.add(Country("Name_4", "Continent_4", 6, 1))
        many_country_catalogue.add(Country("Name_5", "Continent_5", 10, 1))
        self.assertEqual(
            Country("Name_3", "Continent_3", 10, 1), many_country_catalogue.country_with_largest_population_density()
        )

    def test_country_with_smallest_population_density_duplicate_densities_returns_correct_country(self):
        many_country_catalogue = CountryCatalogue()
        many_country_catalogue.add(Country("Name_1", "Continent_1", 5, 1))
        many_country_catalogue.add(Country("Name_2", "Continent_2", 2, 1))
        many_country_catalogue.add(Country("Name_3", "Continent_3", 1, 1))
        many_country_catalogue.add(Country("Name_4", "Continent_4", 6, 1))
        many_country_catalogue.add(Country("Name_5", "Continent_5", 1, 1))
        self.assertEqual(
            Country("Name_3", "Continent_3", 1, 1), many_country_catalogue.country_with_smallest_population_density()
        )

    def test_filter_countries_by_population_density_duplicate_within_range_returns_country_catalogue_all_duplicates(
        self,
    ):
        many_country_catalogue = CountryCatalogue()
        many_country_catalogue.add(Country("Name", "Continent", 10, 1))
        many_country_catalogue.add(Country("Name", "Continent", 10, 1))
        many_country_catalogue.add(Country("Name", "Continent", 10, 1))
        expected = CountryCatalogue()
        expected.add(Country("Name", "Continent", 10, 1))
        expected.add(Country("Name", "Continent", 10, 1))
        expected.add(Country("Name", "Continent", 10, 1))
        filtered_country_catalogue = many_country_catalogue.filter_countries_by_population_density(0, 100)
        self.assertEqual(expected, filtered_country_catalogue)

    def test_most_populous_continent_duplicate_populations_returns_first_continent_found(self):
        many_country_catalogue = CountryCatalogue()
        many_country_catalogue.add(Country("Name_1", "Continent_1", 5, 1))
        many_country_catalogue.add(Country("Name_2", "Continent_1", 2, 1))
        many_country_catalogue.add(Country("Name_3", "Continent_2", 5, 1))
        many_country_catalogue.add(Country("Name_4", "Continent_3", 6, 1))
        many_country_catalogue.add(Country("Name_5", "Continent_3", 1, 1))
        self.assertEqual("Continent_1", many_country_catalogue.most_populous_continent())

    def test_eq_various_equal_cases_are_equal(self):
        empty_a = CountryCatalogue()
        empty_b = CountryCatalogue()
        single_a = CountryCatalogue()
        single_a.add(Country("Name_1", "Continent_1", 5, 1))
        single_b = CountryCatalogue()
        single_b.add(Country("Name_1", "Continent_1", 5, 1))
        many_a = CountryCatalogue()
        many_a.add(Country("Name_1", "Continent_1", 5, 1))
        many_a.add(Country("Name_2", "Continent_2", 2, 1))
        many_a.add(Country("Name_3", "Continent_3", 1, 1))
        many_a.add(Country("Name_4", "Continent_4", 6, 1))
        many_a.add(Country("Name_5", "Continent_5", 1, 1))
        many_b = CountryCatalogue()
        many_b.add(Country("Name_1", "Continent_1", 5, 1))
        many_b.add(Country("Name_2", "Continent_2", 2, 1))
        many_b.add(Country("Name_3", "Continent_3", 1, 1))
        many_b.add(Country("Name_4", "Continent_4", 6, 1))
        many_b.add(Country("Name_5", "Continent_5", 1, 1))
        countries_a = [empty_a, single_a, many_a]
        countries_b = [empty_b, single_b, many_b]
        for country_a, country_b in zip(countries_a, countries_b):
            with self.subTest(country_a=country_a, country_b=country_b):
                self.assertEqual(country_a, country_b)

    def test_eq_various_not_equal_cases_are_not_equal(self):
        empty_a = CountryCatalogue()
        single_a = CountryCatalogue()
        single_a.add(Country("Name_1", "Continent_1", 5, 1))
        single_b = CountryCatalogue()
        single_b.add(Country("Name_100", "Continent_100", 5, 1))
        different_order_a = CountryCatalogue()
        different_order_a.add(Country("Name_1", "Continent_1", 5, 1))
        different_order_a.add(Country("Name_2", "Continent_2", 2, 1))
        different_order_a.add(Country("Name_3", "Continent_3", 1, 1))
        different_order_a.add(Country("Name_4", "Continent_4", 6, 1))
        different_order_a.add(Country("Name_5", "Continent_5", 1, 1))
        different_order_b = CountryCatalogue()
        different_order_b.add(Country("Name_1", "Continent_1", 5, 1))
        different_order_b.add(Country("Name_2", "Continent_2", 2, 1))
        different_order_b.add(Country("Name_3", "Continent_3", 1, 1))
        different_order_b.add(Country("Name_5", "Continent_5", 1, 1))
        different_order_b.add(Country("Name_4", "Continent_4", 6, 1))
        countries_a = [empty_a, single_a, different_order_a, empty_a]
        countries_b = [single_b, single_b, different_order_b, []]
        for country_a, country_b in zip(countries_a, countries_b):
            with self.subTest(country_a=country_a, country_b=country_b):
                self.assertNotEqual(country_a, country_b)

# Run this cell to run all unit tests
unittest.main(argv=[''], verbosity=2, exit=False)

# NAME:
# ST-NUMBER:
# StFX EMAIL:

COUNTRY_DATA_FILE_NAME = "country_data.csv"

# Makes it so the import from the unit tests do not break things
if __name__ == "__main__":
    # Load data
    catalogue = CountryCatalogue()
    in_file = open(COUNTRY_DATA_FILE_NAME, "r")
    for line in in_file:
        split_line = line.split(",")
        country = Country(
            name=split_line[0], continent=split_line[1], population=int(split_line[2]), area=float(split_line[3])
        )
        catalogue.add(country)
    in_file.close()

    # Alter catalogue contents
    england = Country("England", "Europe", 56489800, 130279)
    ecuador = Country("Ecuador", "South America", 18048628, 256370)
    india = Country("India", "Asia", 1375586000, 3287263)
    catalogue.add(england)
    catalogue.add(ecuador)
    catalogue.add(india)
    catalogue.remove(Country("Canada", "North America", 34207000, 9976140.0))
    catalogue.remove(Country("South Korea", "Asia", 50503933, 98076.92))

    # Answering questions
    print(catalogue.country_with_smallest_population_density())
    print(catalogue.country_with_largest_population_density())
    print(catalogue.most_populous_continent())

    # Save filtered data
    filtered_catalogue = catalogue.filter_countries_by_population_density(200, 450)
    out_file = open("density-200_450.csv", "w")
    out_file.write(str(filtered_catalogue))
    out_file.close()