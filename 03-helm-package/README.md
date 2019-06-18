# Install helm-unittest

Repo: [helm-unittest](https://github.com/lrills/helm-unittest)

```
helm plugin install https://github.com/lrills/helm-unittest
```

It will install the latest version of binary into helm plugin directory.

# Test the plugin

The test suite file is written in pure YAML, and default placed under the `tests/` directory of the chart with suffix `_test.yaml`.

The following command renders your charts locally (without tiller) and runs tests defined in test suite files.

```
helm unittest <my-chart>
```

Or specify the suite files glob path pattern.

```
helm unittest -f 'my-tests/*.yaml' <my-chart>
```

In this example, the tests are in `/basic/tests/deployment_test.yaml`.

```
helm unittest --color basic

### Chart [ basic ] basic

 PASS  test deployment	basic/tests/deployment_test.yaml

Charts:      1 passed, 1 total
Test Suites: 1 passed, 1 total
Tests:       3 passed, 3 total
Snapshot:    0 passed, 0 total
Time:        2.626455ms

```

You can see all the command information using the `--help` flag.

```
helm unittest --help

Running chart unittest written in YAML.

This renders your charts locally (without tiller) and
validates the rendered output with the tests defined in
test suite files. Simplest test suite file looks like
below:

---
# CHART_PATH/tests/deployment_test.yaml
suite: test my deployment
templates:
  - deployment.yaml
tests:
  - it: should be a Deployment
    asserts:
      - isKind:
          of: Deployment
---

Put the test files in "tests" directory under your chart
with suffix "_test.yaml", and run:

$ helm unittest my-chart

Or specify the suite files glob path pattern:

$ helm unittest -f 'my-tests/*.yaml' my-chart

Check https://github.com/lrills/helm-unittest for more
details about how to write tests.

Usage:
  unittest [flags] CHART [...]

Flags:
      --color                  enforce printing colored output even stdout is not a tty. Set to false to disable color
  -f, --file stringArray       glob paths of test files location, default to tests/*_test.yaml (default [tests/*_test.yaml])
  -h, --help                   help for unittest
  -u, --update-snapshot        update the snapshot cached if needed, make sure you review the change before update
  -s, --with-subchart charts   include tests of the subcharts within charts folder (default true)

```
