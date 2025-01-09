import coverage
import unittest

def run_tests_and_coverage():
    cov = coverage.Coverage()
    cov.start()

    loader = unittest.TestLoader()
    tests = loader.discover('.')
    test_runner = unittest.TextTestRunner(verbosity=2)
    result = test_runner.run(tests)

    cov.stop()
    cov.save()

    print("\nCoverage Report:")
    cov.report()

    cov.html_report(directory='htmlcov')
    print("\nHTML report generated in the 'htmlcov' directory.")

    if not result.wasSuccessful():
        exit(1)

if __name__ == "__main__":
    run_tests_and_coverage()
