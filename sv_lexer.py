"""An SV plugin lexer for Pygments."""

from pygments.lexer import RegexLexer, bygroups
from pygments.token import Token, Text, Whitespace

Comment = Token.Comment
Constant = Token.Constant
Entity = Token.Entity
Invalid = Token.Invalid
Keyword = Token.Keyword
Meta = Token.Meta
Punctuation = Token.Punctuation
Storage = Token.Storage
String = Token.String
Support = Token.Support

SV_TYPES = {
    Comment:                                    'sv-c',
    Comment.Block:                              'sv-cb',
    Comment.Line:                               'sv-cl',
    Comment.Line.DoubleSlash:                   'sv-cld',
    
    Constant:                                   'sv-co',
    Constant.Character:                         'sv-coc',
    Constant.Character.Escape:                  'sv-coce',
    Constant.Numeric:                           'sv-con',
    Constant.Numeric.Bit:                       'sv-conb',
    Constant.Numeric.Decimal:                   'sv-cond',
    Constant.Numeric.Exp:                       'sv-cone',
    Constant.Numeric.Time:                      'sv-cont',
    Constant.Other:                             'sv-coo',
    Constant.Other.Define:                       'sv-cood',
    Constant.Other.Net:                         'sv-coon',
    Constant.Other.Placeholder:                 'sv-coop',
    Constant.Other.Preprocessor:                'sv-coopr',
    
    Entity:                                     'sv-e',
    Entity.Label:                               'sv-el',
    Entity.Name:                                'sv-en',
    Entity.Name.Declaration:                    'sv-end',
    Entity.Name.Function:                       'sv-enf',
    Entity.Name.Section:                        'sv-ens',
    Entity.Name.Sva:                            'sv-ensv',
    Entity.Name.Type:                           'sv-ent',
    Entity.Name.Type.Class:                     'sv-entc',
    Entity.Name.Type.Define:                     'sv-entd',
    Entity.Name.Type.Module:                    'sv-entm',
    Entity.Other:                               'sv-eo',
    Entity.Other.InheritedClass:                'sv-eoi',
    Entity.Psl:                                 'sv-ep',
    Entity.Psl.Name:                            'sv-epn',
    
    Invalid:                                    'sv-i',
    Invalid.Illegal:                            'sv-ii',
    Invalid.Illegal.Placeholder:                'sv-iip',
    
    Keyword:                                    'sv-k',
    Keyword.Control:                            'sv-kc',
    Keyword.Cover:                              'sv-kco',
    Keyword.Operator:                           'sv-ko',
    Keyword.Operator.Arithmetic:                'sv-koa',
    Keyword.Operator.Bitwise:                   'sv-kob',
    Keyword.Operator.Cast:                      'sv-koc',
    Keyword.Operator.Comparison:                'sv-koco',
    Keyword.Operator.Logical:                   'sv-kol',
    Keyword.Operator.Other:                     'sv-koo',
    Keyword.Operator.Param:                     'sv-kop',
    Keyword.Operator.Scope:                     'sv-kos',
    Keyword.Other:                              'sv-kot',
    Keyword.Other.Block:                        'sv-kotb',
    Keyword.Psl:                                'sv-kp',
    Keyword.Sva:                                'sv-ks',
    
    Meta:                                       'sv-m',
    Meta.Cast:                                  'sv-mc',
    Meta.Define:                                 'sv-md',
    Meta.Definition:                             'sv-mde',
    Meta.Definition.Class:                       'sv-mdec',
    Meta.Function:                              'sv-mf',
    Meta.ModuleParam:                           'sv-mmp',
    Meta.Module:                                'sv-mm',
    Meta.Module.Inst:                           'sv-mmi',
    Meta.Module.Inst.Param:                     'sv-mmip',
    Meta.Object:                                'sv-mo',
    Meta.Object.End:                            'sv-moe',
    Meta.Param:                                 'sv-mp',
    Meta.Psl:                                   'sv-mps',
    Meta.Scope:                                 'sv-ms',
    Meta.Section:                               'sv-mse',
    Meta.Section.Begin:                         'sv-mseb',
    Meta.Sequence:                              'sv-msq',
    Meta.Struct:                                'sv-mst',
    Meta.Struct.Anonymous:                      'sv-msta',
    Meta.Struct.Assign:                         'sv-mstas',
    Meta.Task:                                  'sv-mt',
    Meta.Task.Simple:                           'sv-mts',
    Meta.Typedef:                               'sv-mtyp',
    Meta.Typedef.Class:                         'sv-mtc',
    Meta.Typedef.Simple:                        'sv-mts',
    Meta.Typedef.Struct:                        'sv-mtst',
    Meta.Userdefined:                            'sv-mu',
    
    Punctuation:                                'sv-p',
    Punctuation.Definition:                      'sv-pd',
    Punctuation.Definition.Comment:              'sv-pdc',
    Punctuation.Definition.String:               'sv-pds',
    Punctuation.Definition.String.Begin:         'sv-pdsb',
    Punctuation.Definition.String.End:           'sv-pdse',
    
    Storage:                                    'sv-s',
    Storage.Modifier:                            'sv-sm',
    Storage.Module:                             'sv-smo',
    Storage.Type:                               'sv-sty',
    Storage.Type.Interface:                     'sv-sti',
    Storage.Type.Rand:                          'sv-str',
    Storage.Type.Userdefined:                    'sv-stu',
    Storage.Type.Uvm:                           'sv-stuvm',
    
    String:                                     'sv-st',
    String.Quoted:                              'sv-stq',
    String.Quoted.Double:                       'sv-stqd',
    
    Support:                                    'sv-su',
    Support.Class:                              'sv-suc',
    Support.Constant:                           'sv-suco',
    Support.Function:                           'sv-suf',
    Support.Function.Field:                     'sv-suff',
    Support.Function.Generic:                   'sv-sufg',
    Support.Function.Port:                      'sv-sufp',
    Support.Function.Port.Implicit:             'sv-sufpi',
    Support.Modport:                            'sv-sum',
    Support.Type:                               'sv-sut',
    Support.Type.Scope:                         'sv-suts',
    Support.Variable:                           'sv-suv',
}

class SVLexer(RegexLexer):
    # This should be the human-readable name of the language.  In this example,
    # doing
    #
    #   pygments.lexers.find_lexer_class("Pygments Plugin Example Language")
    #
    # will return the SVLexer class.
    name = "Pygments Plugin SystemVerilog Language"

    # This is a list of names that can be used to select the language.
    # In this example, we can call the pygmentize command as
    #
    #   pygmentize -l example-lang
    #
    # Also, doing
    #
    #   pygments.lexers.find_lexer_class_by_name("example-lang")
    #
    # in Python will find the lexer class. This is what many documentation or
    # site generation tools implicitly do with code blocks, e.g., this in Sphinx
    # reST:
    #
    #   .. code-block:: example-lang
    #
    #      your code here
    #
    # or this in Markdown:
    #
    #   ```example-lang
    #   your code here
    #   ```
    #
    aliases = ["sv-lang", "systemverilog-lang", "sv", "systemverilog"]

    # This is a list of file patterns that will automatically be highlighted
    # with this lexer. In this example, calling
    #
    #   pygmentize file.exmpl
    #
    # will automatically highlight file.exmpl with this lexer, without needing
    # to pass `-l example-lang`. Similarly,
    #
    #   pygments.lexers.find_lexer_class_for_filename("file.exmpl")
    #
    # will return the SVLexer class.
    filenames = ["*.sv", "*.svh"]

    # This is a list of MIME types for the language. In this example,
    #
    #   pygments.lexers.get_lexer_for_mimetype("text/x-exmpl")
    #
    # will return the SVLexer class.
    mimetypes = ["text/x-systemverilog"]
    
    functions = [
        (r'\b(\w+)(?=\s*\()', Support.Function.Generic),
    ]

    constants = [
        (r"(\b\d+)?'(s?[bB]\s*[0-1xXzZ?][0-1_xXzZ?]*|s?[oO]\s*[0-7xXzZ?][0-7_xXzZ?]*|s?[dD]\s*[0-9xXzZ?][0-9_xXzZ?]*|s?[hH]\s*[0-9a-fA-FxXzZ?][0-9a-fA-F_xXzZ?]*)((e|E)(\+|-)?[0-9]+)?(?!'|\w)", Constant.Numeric),
        (r"'[01xXzZ]", Constant.Numeric.Bit),
        (r'\b((\d[\d_]*)(e|E)(\+|-)?[0-9]+)\b', Constant.Numeric.Exp),
        (r'\b(\d[\d_]*)\b', Constant.Numeric.Decimal),
        (r'\b(\d+(fs|ps|ns|us|ms|s)?)\b', Constant.Numeric.Time),
        (r'\b([A-Z][A-Z0-9_]*)\b', Constant.Other.Net),
        (r'(`ifdef|`ifndef|`default_nettype)(?:\s+)(\w+)', bygroups(Constant.Other.Preprocessor, Support.Variable)),
        (r'`(celldefine|else|elsif|endcelldefine|endif|include|line|nounconnected_drive|resetall|timescale|unconnected_drive|undef|begin_\w+|end_\w+|remove_\w+|restore_\w+)\b', Constant.Other.Preprocessor),
        (r'`\b([a-zA-Z_][a-zA-Z0-9_]*)\b', Constant.Other.Define),
        (r'\b(null)\b', Support.Constant),
    ]

    operators = [
        (r'(=|==|===|!=|!==|<=|>=|<|>)', Keyword.Operator.Comparison),
        (r'(\-|\+|\*|\/|%)', Keyword.Operator.Arithmetic),
        (r'(!|&&|\|\||\bor\b)', Keyword.Operator.Logical),
        (r"(&|\||\^|~|{|'{|}|<<|>>|\?|:)", Keyword.Operator.Bitwise),
        (r'(#|@)', Keyword.Operator.Other),
    ]

    comments = [
        (r'/\*', Punctuation.Definition.Comment, 'comment'),
        (r'(//)(.*$\n?)', bygroups(Punctuation.Definition.Comment, Comment.Line.DoubleSlash))
    ]

    portDir = [
        # match ports with size declarations
        (r'(?:\s*\b)(output|input|inout|ref)(?:\s+)(?:([a-zA-Z_][a-zA-Z0-9_]*)(::))?([a-zA-Z_][a-zA-Z0-9_]*)?(?:\s+)(?=\[[a-zA-Z0-9_\-\+]*:[a-zA-Z0-9_\-\+]*\]\s+[a-zA-Z_][a-zA-Z0-9_\s]*)', bygroups(Support.Type, Support.Type.Scope, Keyword.Operator.Scope, Storage.Type.Interface)),
        # match ports without size declarations
        (r'(?:\s*\b)(output|input|inout|ref)(?:\s+)(?:([a-zA-Z_][a-zA-Z0-9_]*)(::))?([a-zA-Z_][a-zA-Z0-9_]*)?(?:\s+)(?=[a-zA-Z_][a-zA-Z0-9_\s]*)', bygroups(Support.Type, Support.Type.Scope, Keyword.Operator.Scope, Storage.Type.Interface)),
        (r'\s*\b(output|input|inout|ref)\b', Support.Type),
    ]
    
    storageType = [
        (r'\s*\b(var|wire|tri|tri[01]|supply[01]|wand|triand|wor|trior|trireg|reg|integer|int|longint|shortint|logic|bit|byte|shortreal|string|time|realtime|real|process|void)\b', Storage.Type),
        (r'\s*\b(uvm_transaction|uvm_component|uvm_monitor|uvm_driver|uvm_test|uvm_env|uvm_object|uvm_agent|uvm_sequence_base|uvm_sequence|uvm_sequence_item|uvm_sequence_state|uvm_sequencer|uvm_sequencer_base|uvm_component_registry|uvm_analysis_imp|uvm_analysis_port|uvm_analysis_export|uvm_config_db|uvm_active_passive_enum|uvm_phase|uvm_verbosity|uvm_tlm_analysis_fifo|uvm_tlm_fifo|uvm_report_server|uvm_objection|uvm_recorder|uvm_domain|uvm_reg_field|uvm_reg|uvm_reg_block|uvm_bitstream_t|uvm_radix_enum|uvm_printer|uvm_packer|uvm_comparer|uvm_scope_stack)\b', Storage.Type.Uvm),
    ]
    
    storageScope = [
        (r'(\b[a-zA-Z_][a-zA-Z0-9_]*)(::)', bygroups(Support.Type, Keyword.Operator.Scope)),
    ]
    
    storageModifier = [
        (r'\b(signed|unsigned|small|medium|large|supply[01]|strong[01]|pull[01]|weak[01]|highz[01])\b', Storage.Modifier),
    ]
    
    ifmodport = [
        # interface with modport declaration
        (r'(\b[a-zA-Z_][a-zA-Z0-9_]*)(?:\.)([a-zA-Z_][a-zA-Z0-9_]*\s+)([a-zA-Z_][a-zA-Z0-9_]*\b)', bygroups(Storage.Type.Interface, Support.Modport)),
    ]

    strings = [
        (r'"', Punctuation.Definition.String.Begin, 'string'),
        (r'\\.', Constant.Character.Escape),
        (r'(?x)%'
            r'(\d+\$)?'                             # field (argument #)
            r"[#0\- +']*"                           # flags
            r'[,;:_]?'                              # separator character (AltiVec)
            r'((-?\d+)|\*(-?\d+\$)?)?'              # minimum field width
            r'(\.((-?\d+)|\*(-?\d+\$)?)?)?'         # precision
            r'(hh|h|ll|l|j|t|z|q|L|vh|vl|v|hv|hl)?' # length modifier
            r'[bdiouxXhHDOUeEfFgGaACcSspnmt%]'      # conversion type')
            , Constant.Other.Placeholder),
        (r'%', Invalid.Illegal.Placeholder),
    ]
    
    moduleBinding = [
        (r'(?:\.)([a-zA-Z_][a-zA-Z0-9_]*)(?:\s*\()', bygroups(Support.Function.Port), 'modulebinding'),
        (r'(?:\.)([a-zA-Z_][a-zA-Z0-9_]*\s*)', bygroups(Support.Function.Port.Implicit))
    ]
    
    moduleParam = [
        (r'(#)(?:\s*\()', bygroups(Keyword.Operator.Param), 'moduleparam'),
    ]

    allTypes = storageType + storageModifier

    baseGrammar = allTypes + comments + operators + constants + strings + [
        (r'^\s*([a-zA-Z_][a-zA-Z0-9_]*)\s+[a-zA-Z_][a-zA-Z0-9_,=\s]*', Storage.Type.Interface)
    ] + storageScope
    
    structAnonymous = [
        (r'(?:\s*\b)(struct|union)(?:\s*)(packed)?(?:\s*)', bygroups(Keyword.Control, Keyword.Control), 'structanonymous')
    ] + baseGrammar

    # This lexer highlights lines that read "foo".
    tokens = {
        'root': [
            (r'\s+', Whitespace),
            # functions/tasks
            (r'(?:\s*\b)(function|task)(?:\b)(\s+automatic)?', bygroups(Keyword.Control, Keyword.Control), 'function'),
            (r'(?:\s*\b)(task)(?:\s+)(automatic)?(?:\s*)(\w+)(?:\s*;)', bygroups(Keyword.Control, Keyword.Control, Entity.Name.Function)),
            # structs
            (r'(\s*\btypedef\s+)(struct|enum|union)(?:\b\s*)(packed)?(?:\s*)([a-zA-Z_][a-zA-Z0-9_]*)?', bygroups(Keyword.Control, Keyword.Control, Keyword.Control, Storage.Type), 'struct'),
            # typedef class
            (r'(\s*\btypedef\s+class\s+)([a-zA-Z_][a-zA-Z0-9_]*)(?:\s*;)', bygroups(Keyword.Control, Entity.Name.Declaration)),
            # typedef simple
            (r'\s*\btypedef\b', Keyword.Control, 'typedef'),
            # module declaration
            (r'(\s*module\s+\b)([a-zA-Z_][a-zA-Z0-9_]*\b)', bygroups(Keyword.Control, Entity.Name.Type.Module), 'module'),
            # sequence
            (r'(\bsequence\s+)([a-zA-Z_][a-zA-Z0-9_]*)', bygroups(Keyword.Control, Entity.Name.Function)),
            # bing directive
            (r'(\bbind\s+)([a-zA-Z_][a-zA-Z0-9_\.]*\b)', bygroups(Keyword.Control)),
            # labeled block
            (r'(?:\s*)(begin|fork)(\s*:\s*)([a-zA-Z_][a-zA-Z0-9_]*\b)', bygroups(Keyword.Other.Block, Keyword.Operator, Entity.Name.Section)),
            # sva property
            (r'(\bproperty\s+)(\w+)', bygroups(Keyword.Sva, Entity.Name.Sva)),
            # sva assert
            (r'(\b\w+)(\s*:\s*)(assert\b)', bygroups(Entity.Name.Sva, Keyword.Operator, Keyword.Sva)),
            # psl one-liner
            (r'(\s*//\s*)(psl\s+)(?:(\w+)\s*(:))?(?:\s*)(default|assert|assume)', bygroups(Comment.Line.DoubleSlash, Keyword.Psl, Entity.Psl.Name, Keyword.Operator, Keyword.Psl), 'psl'),
            # psl multiline
            (r'(\s*/\*\s*)(psl)', bygroups(Comment.Block, Keyword.Psl), 'pslmulti'),
            # keyword
            (r'(?:\s*\b)(automatic|cell|config|deassign|defparam|design|disable|edge|endconfig|endgenerate|endspecify|endtable|event|generate|genvar|ifnone|incdir|instance|liblist|library|macromodule|negedge|noshowcancelled|posedge|pulsestyle_onevent|pulsestyle_ondetect|scalared|showcancelled|specify|specparam|table|use|vectored)(?:\b)', bygroups(Keyword.Other)),
            (r'(?:\s*\b)(initial|always|wait|force|release|assign|always_comb|always_ff|always_latch|forever|repeat|while|for|if|iff|else|case|casex|casez|default|endcase|return|break|continue|do|foreach|with|inside|dist|clocking|cover|coverpoint|property|bins|binsof|illegal_bins|ignore_bins|randcase|modport|matches|solve|static|assert|assume|before|expect|cross|ref|first_match|srandom|struct|packed|final|chandle|alias|tagged|extern|throughout|timeprecision|timeunit|priority|type|union|uwire|wait_order|triggered|randsequence|import|export|context|pure|intersect|wildcard|within|new|typedef|enum|this|super|begin|fork|forkjoin|unique|unique0|priority)(?:\b)', bygroups(Keyword.Control)),
            (r'(?:\s*\b)(end|endtask|endmodule|endfunction|endprimitive|endclass|endpackage|endsequence|endprogram|endclocking|endproperty|endgroup|endinterface|join|join_any|join_none)(?:\b)(?:\s*(:)\s*(\w+))?', bygroups(Keyword.Control, Keyword.Operator, Entity.Label)),
            (r'\b(std)\b::', Support.Class),
            (r'(^\s*`define\s+)([a-zA-Z_][a-zA-Z0-9_]*)', bygroups(Constant.Other.Define, Entity.Name.Type.Define))
        ] + comments + [
            (r'(?:\s*)(primitive|package|constraint|interface|covergroup|program)(\s+\b[a-zA-Z_][a-zA-Z0-9_]*\b)', bygroups(Keyword.Control, Entity.Name.Type.Class)),
            (r'(?:([a-zA-Z_][a-zA-Z0-9_]*)\s*(:))?(?:\s*)(coverpoint|cross)(\s+[a-zA-Z_][a-zA-Z0-9_]*)', bygroups(Entity.Name.Type.Class, Keyword.Operator.Other, Keyword.Control)),
            (r'(?:\b)(virtual\s+)?(class\s+)(\b[a-zA-Z_][a-zA-Z0-9_]*\b)', bygroups(Keyword.Control, Keyword.Control, Entity.Name.Type.Class)),
            (r'(\bextends\s+)([a-zA-Z_][a-zA-Z0-9_]*\b)', bygroups(Keyword.Control, Entity.Other.InheritedClass))
        ] + allTypes + operators + portDir + [
            (r'\b(and|nand|nor|or|xor|xnor|buf|not|bufif[01]|notif[01]|r?[npc]mos|tran|r?tranif[01]|pullup|pulldown)\b', Support.Type)
        ] + strings + [
            (r'\$\b([a-zA-Z_][a-zA-Z0-9_]*)\b', Support.Function),
            # cast operator
            (r"(\b[a-zA-Z_][a-zA-Z0-9_]*)(')(?=\()", bygroups(Storage.Type, Keyword.Operator.Cast)),
            # parameter/localparameter with no type in uppercase
            (r'(?:^\s*)(localparam|parameter)(\s+[A-Z_][A-Z0-9_]*\b\s*)(?=(=))', bygroups(Keyword.Other, Constant.Other)),
            # parameter/localparameter with no type
            (r'(?:^\s*)(localparam|parameter)(\s+[a-zA-Z_][a-zA-Z0-9_]*\b\s*)(?=(=))', bygroups(Keyword.Other)),
            # variable/parameter/localparameter with user-defined type
            (r"(?:^\s*)(local\s+|protected\s+|localparam\s+|parameter\s+)?(const\s+|virtual\s+)?(rand\s+|randc\s+)?(?:([a-zA-Z_][a-zA-Z0-9_]*)(::))?([a-zA-Z_][a-zA-Z0-9_]*\b\s*)(?=(#\s*\([\w,]+\)\s*)?([a-zA-Z][a-zA-Z0-9_\s\[\]']*)(;|,|=|'\{))", bygroups(Keyword.Other, Keyword.Other, Storage.Type.Rand, Support.Type.Scope, Keyword.Operator.Scope, Storage.Type.Userdefined)),
            (r'(\s*\boption)(?:\.)', bygroups(Keyword.Cover)),
            (r'(?:\s*\b)(local|const|protected|virtual|localparam|parameter)(?:\b)', bygroups(Keyword.Other)),
            (r'(?:\s*\b)(rand|randc)(?:\b)', Storage.Type.Rand),
            # module instantiation with parameter
            (r'(?:^)(?:\s*(bind)\s+([a-zA-Z_][\w\.]*))?(\s*[a-zA-Z_][a-zA-Z0-9_]*\s*)(?=#[^#])', bygroups(Keyword.Control, None, Storage.Module), 'moduleinstparam'),
            # module instantiation with no param
            (r'(\b[a-zA-Z_][a-zA-Z0-9_]*\s+)(?!intersect|and|or|throughout|within)([a-zA-Z_][a-zA-Z0-9_]*\s*)(?:\[(\d+)(?:\:(\d+))?\])?\s*(\(|$)', bygroups(Storage.Module, Entity.Name.Type.Module, Constant.Numeric, Constant.Numeric), 'moduleinstnoparam'),
            # struct assignement (could also match array assignment)
            (r"(\b\s+&lt;?=\s*)(\'{)", bygroups(Keyword.Operator.Other, Keyword.Operator.Other, Keyword.Operator.Other), 'structassign')
        ] + storageScope + functions + constants,
        'function': [
            (r';', Text, '#pop'),
            (r'(?:\b)([a-zA-Z_][a-zA-Z0-9_]*\s+)?([a-zA-Z_][a-zA-Z0-9_:]*\s*)(?=\(|;)', bygroups(Storage.Type, Entity.Name.Function)),
        ] + portDir + baseGrammar,
        'struct': [
            (r'(}\s*)([a-zA-Z_][a-zA-Z0-9_]*)(?:\s*;)', bygroups(Keyword.Operator.Other, Entity.Name.Function), '#pop'),
        ] + structAnonymous + baseGrammar,
        'typedef': [
            (r'([a-zA-Z_][a-zA-Z0-9_]*\s*)(?=(\[[a-zA-Z0-9_:\$\-\+]*\])?;)', bygroups(Entity.Name.Function), '#pop'),
            (r'(\b[a-zA-Z_]\w*\s*)(#)\(', bygroups(Storage.Type.Userdefined, Keyword.Operator.Param))
        ] + baseGrammar + moduleBinding,
        'module': [
            (r';', Text, '#pop'),
        ] + portDir + [
            (r'\s*(parameter)', Keyword.Other)
        ] + baseGrammar + ifmodport,
        'psl': [
            (r';', Text, '#pop'),
            (r'\b(never|always|default|clock|within|rose|fell|stable|until|before|next|eventually|abort|posedge)\b', Keyword.Psl),
        ] + operators + functions + constants,
        'pslmulti': [
            (r'(\*/)', bygroups(Comment.Block), '#pop'),
            (r'(?:^\s*)(?:(\w+)\s*(:))?(?:\s*)(default|assert|assume)', bygroups(Entity.Psl.Name, Keyword.Operator, Keyword.Psl)),
            (r'(\bproperty\s+)(\w+)', bygroups(Keyword.Psl, Entity.Psl.Name)),
            (r'\b(never|always|default|clock|within|rose|fell|stable|until|before|next|eventually|abort|posedge|negedge)\b', Keyword.Psl),
        ] + operators + functions + constants,
        'moduleinstparam': [
            (r'(?=;|=|:)', Text, '#pop'),
        ] + moduleBinding + moduleParam + comments + operators + constants + strings + [
            (r'\b([a-zA-Z_][a-zA-Z0-9_]*)\b(?=\s*(\(|$))', Entity.Name.Type.Module)
        ],
        'moduleinstnoparam': [
            (r';', Text, '#pop')
        ] + moduleBinding + comments + strings + operators + constants,
        'structassign': [
            (r';', Text, '#pop'),
            (r'(\b\w+\s*)(:)(?!:)', bygroups(Support.Function.Field, Keyword.Operator.Other))
        ] + comments + strings + operators + constants + storageScope,
        'comment': [
            (r'\*/', Comment.Block, '#pop'),
        ],
        'string': [
            (r'"', Punctuation.Definition.String.End, '#pop'),
        ],
        'modulebinding': [
            (r'\)', Text, '#pop'),
        ] + constants + comments + operators + strings + [
            (r'(\b[a-zA-Z_]\w*)(::)', bygroups(Support.Type.Scope, Keyword.Operator.Scope)),
            (r"(\b[a-zA-Z_]\w*)(')", bygroups(Storage.Type.Interface, Keyword.Operator.Cast)),
            (r'\$\b([a-zA-Z_][a-zA-Z0-9_]*)\b', Support.Function),
            (r'\b(virtual)\b', Keyword.Control)
        ],
        'moduleparam': [
            (r'\)', Text, '#pop'),
        ] + comments + constants + operators + strings + moduleBinding + [
            (r'\b(virtual)\b', Keyword.Control)
        ],
        'structanonymous': [
            (r'(})(\s*[a-zA-Z_]\w*)(?:\s*;)', bygroups(Keyword.Operator.Other), '#pop'),
        ]
    }
