{
	'variables' : {
		'node_shared': 'true',
		'WIN_VER' : 'v10',
		'WIN_SDK_VER' : '10.0.15063.0',
		'VS_VER': '14.0',
	},
    'target_defaults': {
        'default_configuration': 'Release',
        'configurations': {
            'Debug': {
                'msvs_settings': {
                    'VCCLCompilerTool': {
                        'ExceptionHandling': 1, # /EHsc,
                        'RuntimeLibrary': '3', # /MDd
                    }
                }
		    },
            'Release': {
                'msvs_settings': {
                    'VCCLCompilerTool': {
                        'ExceptionHandling': 1, # /EHsc,
                        'RuntimeLibrary': '2', # /MD
                    }
                }
            }
        }
    }
}