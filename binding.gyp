{
  "includes": [ "deps/common-sqlite.gypi" ],
  "variables": {
      "sqlite%":"internal",
      "sqlite_libname%":"sqlite3"
  },
  "targets": [
    {
      "target_name": "sqlite",
      "cflags!": [ "-fno-exceptions" ],
      "cflags_cc!": [ "-fno-exceptions" ],
      "xcode_settings": { "GCC_ENABLE_CPP_EXCEPTIONS": "YES",
        "CLANG_CXX_LIBRARY": "libc++",
        "MACOSX_DEPLOYMENT_TARGET": "10.7",
      },
      "msvs_settings": {
        "VCCLCompilerTool": { "ExceptionHandling": 1 },
      },
      "include_dirs": [
        "<!@(node -p \"require('node-addon-api').include\")"],
      "conditions": [
        ["sqlite != 'internal'", {
            "include_dirs": [
              "<!@(node -p \"require('node-addon-api').include\")", "<(sqlite)/include" ],
            "libraries": [
               "-l<(sqlite_libname)"
            ],
            "conditions": [ [ "OS=='linux'", {"libraries+":["-Wl,-rpath=<@(sqlite)/lib"]} ] ],
            "conditions": [ [ "OS!='win'", {"libraries+":["-L<@(sqlite)/lib"]} ] ],
            'msvs_settings': {
              'VCLinkerTool': {
                'AdditionalLibraryDirectories': [
                  '<(sqlite)/lib'
                ],
              },
            }
        },
        {
            "dependencies": [
              "<!(node -p \"require('node-addon-api').gyp\")",
              "deps/sqlite3.gyp:sqlite3"
            ]
        }
        ],
        [ "target_arch=='arm'", {"type": "static_library"} ]
      ],
      "sources": [
        "src/backup.cc",
        "src/database.cc",
        "src/node_sqlite3.cc",
        "src/statement.cc"
      ],
      "defines": [ "NAPI_VERSION=6", "NAPI_DISABLE_CPP_EXCEPTIONS=1", "NAPI_EXPERIMENTAL" ]
    }
  ]
}
