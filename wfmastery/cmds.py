import urllib

from collections import defaultdict
from wfmastery import App



@App.cli.command("list_routes")
def list_routes():
    """
        Roll through Flask's URL rules and print them out
        Thank you to Jonathan Tushman
            And Thank you to Roger Pence
            Sourced http://flask.pocoo.org/snippets/117/ "Helper to list routes (like Rail's rake routes)"

        Note that a lot has possibly changed since that snippet and rule classes have a __str__
            which greatly simplifies all of this
    """


    format_str = lambda *x: "{:30s} {:40s} {}".format(*x)#pylint: disable=W0108
    clean_map = defaultdict(list)


    for rule in App.url_map.iter_rules():
        methods = ",".join(rule.methods)
        clean_map[rule.endpoint].append((methods, str(rule),))

    print(format_str("View handler", "HTTP METHODS", "URL RULE"))
    print("-"*80)
    for endpoint in sorted(clean_map.keys()):
        for rule, methods in sorted(clean_map[endpoint], key=lambda x: x[1]):
            print(format_str(endpoint, methods, rule))
