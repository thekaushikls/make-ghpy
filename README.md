# make-ghpy
###### Github Action to create Grasshopper-Python `.ghpy` plugin.
[![Test Action](https://github.com/thekaushikls/make-ghpy/actions/workflows/test_action.yml/badge.svg)](https://github.com/thekaushikls/make-ghpy/actions/workflows/test_action.yml)
[![Dispatch Action](https://github.com/thekaushikls/make-ghpy/actions/workflows/dispatch_action.yml/badge.svg)](https://github.com/thekaushikls/make-ghpy/actions/workflows/dispatch_action.yml)
[![release)](https://img.shields.io/github/v/release/thekaushikls/make-ghpy?include_prereleases)](https://github.com/thekaushikls/make-ghpy/releases/latest)
[![GitHub](https://img.shields.io/github/license/thekaushikls/make-ghpy)](https://github.com/thekaushikls/make-ghpy/blob/main/LICENSE)

* Collects all python (.py) files recursively from the specified `source` folder.
* Uses `CLR` to compile to a `.ghpy` (or `.dll`) binary.
* Outputs 
  1. `name` of the compiled binary _(without file extension)_
  2. `full-name` of the compiled binary.
  3. `build` of the compiled binary for downstream use.
  

## 🚀 Quick reference
``` YML
- uses: thekaushikls/make-ghpy@v1.0.1
  with:
    source: src
    package-name: my_plugin
    version: 0.0.1
    type: ghpy
    ironpython: true
```

## 🎛️ Usage
See [test_action.yml](.github/workflows/test_action.yml) for example.

``` YML
- uses: thekaushikls/make-ghpy@v1.0.1
  with:
  
    # Root folder for python source.
    source: ''
    
    # Name of the compiled binary / plugin.
    package-name: ''
    
    # Version tag to add with name. For example: v0.0.1
    # Can also add version from tag. For example, ${{ github.ref_name }}
    version: ''
    
    # (Optional) Specifies file type of the compiled binary. Can be 'ghpy' / 'dll'
    # Default: 'ghpy'
    type: ''
    
    # (Optional) If true, installs IronPython v2.7.12 internally.
    # Default: false
    ironpython: ""
```

## 🔥️ Motivation
The motivation comes from my previous [script](https://gist.github.com/thekaushikls/58a0727a86fb2e74121a782e123d163e) where I compile Grasshopper-Python `.ghpy` plugins outside Rhino. This GitHub Action's aim is to take things one step forward by making way for a "build-test-deploy" workflow.

Most folks in the AEC industry prefer python to start programming, and creating custom tools/components. This tool aims to help build and share those a tad bit easier.

## 📃 Resources
1. [Tutorial: creating a Grasshopper component with the Python GHPY compiler](https://discourse.mcneel.com/t/tutorial-creating-a-grasshopper-component-with-the-python-ghpy-compiler/38552)
2. [GitHub Gist: build_module.py](https://gist.github.com/thekaushikls/58a0727a86fb2e74121a782e123d163e)


## ❌ Limitations
1. Users cannot set files / file-patterns to be ignored while compiling.


## 🌱 License
The scripts and documentation in this project are released under the [MIT License](https://github.com/thekaushikls/make-ghpy/blob/main/LICENSE)
