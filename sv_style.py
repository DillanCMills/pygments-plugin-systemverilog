"""An SV plugin style for Pygments."""

from pygments.style import Style
from pygments.token import Token

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

colors = {
    "black": "#000000",
    "black2": "#242424",
    "black3": "#420e09",
    "black4": "#003000",
    "black5": "#0e2231",
    "blue": "#89bdff",
    "blue2": "#3060c0",
    "blue3": "#0050a0",
    "blue4": "#3387cc",
    "blue5": "#5070a8",
    "blue6": "#afc4db",
    "blue7": "#8b98ab",
    "blue8": "#8996a8",
    "blue9": "#8693a5",
    "blue10": "#578bb3",
    "blue11": "#001155",
    "blue12": "#70a8b8",
    "cyan": "#8edcc5",
    "green": "#258022",
    "green2": "#60a633",
    "green3": "#99cf50",
    "green4": "#253b22",
    "grey": "#8a9a95",
    "grey2": "#b1b3ba",
    "grey3": "#c0c0c0",
    "grey4": "#a7a7a7",
    "grey5": "#494949",
    "grey6": "#676767",
    "orange": "#cda869",
    "orange2": "#e9c062",
    "orange3": "#f0c090",
    "orange4": "#cf7d34",
    "orange5": "#9b5c2e",
    "orange6": "#e0c040",
    "orange7": "#dd7b3b",
    "orange8": "#9b703f",
    "orange9": "#fee09c",
    "orange10": "#c5af75",
    "orange11": "#c8b060",
    "orange12": "#e1d4b9",
    "pink": "#fd5ff1",
    "pink2": "#b060a0",
    "pink3": "#562d56",
    "pink4": "#9b859d",
    "purple": "#ae81ff",
    "purple2": "#9080ff",
    "red": "#751012",
    "red2": "#cf6a4c",
    "red3": "#e28964",
    "red4": "#e18964",
    "white": "#ffffff",
    "white2": "#f8f8f8",
    "white3": "#eeeeee",
    "white4": "#cae2fb",
    "white5": "#ddf0ff",
    "yellow": "#f9ee98",
    "yellow2": "#dad085",
    "yellow3": "#ddf2a4",
    "yellow4": "#daefa3",
    "yellow5": "#4a410d",
    "yellow6": "#75715e",
    "yellow7": "#8f9d6a"
}
colorMods = {
    "foreground": colors["white2"],
    "background": colors["black"],
    "caret": colors["grey4"],
    "invisibles": f"{colors['white4']}",
    "line_highlight": f"{colors['white']}",
    "selection": f"{colors['white5']}",
    "selection_border": f"{colors['blue3']}",
    "inactive_selection": f"{colors['white5']}",
    "highlight": f"{colors['blue3']}",
    "brackets_foreground": colors["white"]
}

class SVStyle(Style):
    styles = {
        Comment: f"italic {colors['yellow6']}",
        Punctuation.Definition.Comment: f"italic {colors['yellow6']}",
        Constant.Numeric: colors['blue4'],
        Constant: colors['purple'],
        Constant.Other.Define: colors['purple2'],
        Entity.Name.Type.Constant: colors['purple2'],
        Entity: colors['blue'],
        Keyword: colors['red3'],
        Keyword.Operator: colors['orange6'],
        Storage: colors['green3'],
        String: colors['green'],
        Punctuation.Definition.String: colors['green'],
        Support: colors['pink4'],
        # Variable.Parameter: f"italic {colors['blue2']}",
        # Variable.Language: f"italic {colors['purple2']}",
        # Variable.Other.Member: f"italic {colors['pink2']}",
        Invalid.Deprecated: f"italic underline {colors['pink']}",
        Invalid.Illegal: f"bg:{colors['pink3']} {colors['pink']}",
        Punctuation: colors['grey3'],
        Punctuation.Definition.Variable: colors['blue5'],
        # TextSource: f"bg:{colors['grey2']}",
        Entity.Other.InheritedClass: f"italic {colors['orange5']}",
        String.QuotedSource: colors['yellow4'],
        # StringConstant: colors['yellow3'],
        String.Regexp: colors['orange2'],
        String.RegexpConstant.Character.Escape: colors['orange4'],
        String.RegexpSource.Ruby.Embedded: colors['orange4'],
        String.RegexpString.Regexp.ArbitraryRepetition: colors['orange4'],
        # StringVariable: colors['grey'],
        # Variable.Function: colors['orange11'],
        Support.Function: colors['yellow2'],
        Support.Constant: colors['red2'],
        Support.Function.Field: colors['blue12'],
        Meta.Preprocessor: colors['blue8'],
        Meta.PreprocessorKeyword: colors['blue6'],
        Meta.Cast: f"italic {colors['grey6']}",
        Entity.Name.Tag.Yaml: colors['blue'],
        # Source.YamlString.Unquoted: colors['white3'],
        Meta.Sgml.HtmlMeta.Doctype: colors['grey5'],
        Meta.Sgml.HtmlMeta.DoctypeEntity: colors['grey5'],
        Meta.Sgml.HtmlMeta.DoctypeString: colors['grey5'],
        Meta.XmlProcessing: colors['grey5'],
        Meta.XmlProcessingEntity: colors['grey5'],
        Meta.XmlProcessingString: colors['grey5'],
        Meta.Tag: colors['blue'],
        Meta.TagEntity: colors['blue'],
        # SourceEntity.Name.Tag: colors['orange3'],
        # SourceEntity.Other.AttributeName: colors['orange3'],
        Meta.Tag.Inline: colors['orange3'],
        Meta.Tag.InlineEntity: colors['orange3'],
        Entity.Name.Tag.Namespace: colors['red4'],
        Entity.Other.AttributeName.Namespace: colors['red4'],
        Meta.Selector.CssEntity.Name.Tag: colors['orange'],
        Meta.Selector.CssEntity.Other.AttributeName.Tag.PseudoClass: colors['yellow7'],
        Meta.Selector.CssEntity.Other.AttributeName.Id: colors['blue7'],
        Meta.Selector.CssEntity.Other.AttributeName.Class: colors['orange8'],
        Support.Type.PropertyName.Css: colors['orange10'],
        Meta.PropertyGroupSupport.Constant.PropertyValue.Css: colors['yellow'],
        Meta.PropertyValueSupport.Constant.PropertyValue.Css: colors['yellow'],
        Meta.Preprocessor.AtRuleKeyword.Control.AtRule: colors['blue9'],
        Meta.PropertyValueSupport.Constant.NamedColor.Css: colors['orange7'],
        Meta.PropertyValueConstant: colors['orange7'],
        Meta.Constructor.Argument.Css: colors['yellow7'],
        Meta.Diff: f"italic bg:{colors['black5']} {colors['white2']}",
        Meta.Diff.Header: f"italic bg:{colors['black5']} {colors['white2']}",
        # Markup.Deleted: f"bg:{colors['black3']} {colors['white2']}",
        # Markup.Changed: f"bg:{colors['yellow5']} {colors['white2']}",
        # Markup.Inserted: f"bg:{colors['green4']} {colors['white2']}",
        # Markup.Italic: f"italic {colors['orange2']}",
        # Markup.Bold: f"bold {colors['orange2']}",
        # Markup.Underline: f"underline {colors['red4']}",
        # Markup.Quote: f"italic bg:{colors['orange9']} {colors['orange12']}",
        # Markup.Heading: f"bg:{colors['blue11']} {colors['cyan']}",
        # Markup.HeadingEntity: f"bg:{colors['blue11']} {colors['cyan']}",
        # Markup.List: colors['orange12'],
        # Markup.Raw: f"bg:{colors['grey2']} {colors['blue10']}",
        # MarkupComment: f"italic {colors['yellow6']}",
        Meta.Separator: f"bg:{colors['black2']} {colors['green2']}",
        Meta.Line.Entry.Logfile: f"bg:{colors['white3']}",
        Meta.Line.Exit.Logfile: f"bg:{colors['white3']}",
        Meta.Line.Error.Logfile: f"bg:{colors['red']}",
        Meta.Psl.Systemverilog: f"bg:{colors['black4']}",
        Meta.Psl.Vhdl: f"bg:{colors['black4']}",
        # Source.JsonMeta.Mapping.Key.JsonString.Quoted.Double.Json: colors['orange7'],
        # Source.JsonMeta.Mapping.Value.JsonMeta.Mapping.Key.JsonString.Quoted.Double.Json: colors['orange4'],
        # Source.JsonMeta.Mapping.Value.JsonMeta.Mapping.Value.JsonMeta.Mapping.Key.JsonString.Quoted.Double.Json: colors['orange'],
    }
