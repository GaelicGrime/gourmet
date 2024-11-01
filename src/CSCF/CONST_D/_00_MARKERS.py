

#
#
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# start of CSCF.CONST_D.MARKERS
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
#
#


NEWLINE = "\n"
CMNTLEN = 250
FOLDLEN = 250


FOLD1ENDHERE = f"""# fold here {"⟰1" * (FOLDLEN // 2)}"""
FOLD1ENDHERELN = f"""# fold here {"⟰1" * (FOLDLEN // 2)}{NEWLINE}"""
FOLD1STARTHERE = f"""# fold here {"⟱1" * (FOLDLEN // 2)}"""
FOLD1STARTHERELN = f"""# fold here {"⟱1" * (FOLDLEN // 2)}{NEWLINE}"""
FOLD2ENDHERE = f"""# fold here {"⟰2" * (FOLDLEN // 2)}"""
FOLD2ENDHERELN = f"""# fold here {"⟰2" * (FOLDLEN // 2)}{NEWLINE}"""
FOLD2STARTHERE = f"""# fold here {"⟱2" * (FOLDLEN // 2)}"""
FOLD2STARTHERELN = f"""# fold here {"⟱2" * (FOLDLEN // 2)}{NEWLINE}"""
FOLD3ENDHERE = f"""# fold here {"⟰3" * (FOLDLEN // 2)}"""
FOLD3ENDHERELN = f"""# fold here {"⟰3" * (FOLDLEN // 2)}{NEWLINE}"""
FOLD3STARTHERE = f"""# fold here {"⟱3" * (FOLDLEN // 2)}"""
FOLD3STARTHERELN = f"""# fold here {"⟱3" * (FOLDLEN // 2)}{NEWLINE}"""


CMNTLINE = f"""# * {"#*" * (CMNTLEN // 2)}"""
IMPORTANTSTR = f"""# * {"!-" * (CMNTLEN // 2)}"""  # important line marker
INDENTIN = " -=> "  # display arrow RIGHT
INDENTOUT = " <=- "  # display arrow LEFT
INFOSTR = f"""# * {"%_" * (CMNTLEN // 2)}"""  # INFO _STR_ line


MARK0END = lambda __TAG__: f"""# {"⟰0 " * (CMNTLEN // 3)} {__TAG__}"""
MARK0ENDLN = lambda __TAG__: f"""# {"⟰0 " * (CMNTLEN // 3)} {__TAG__}{NEWLINE}"""
MARK0MID = lambda __TAG__: f"""# {"⟰0⟱ " * (CMNTLEN // 4)} {__TAG__}"""
MARK0MIDLN = lambda __TAG__: f"""# {"⟰0⟱ " * (CMNTLEN // 4)} {__TAG__}{NEWLINE}"""
MARK0START = lambda __TAG__: f"""# {"0⟱ " * (CMNTLEN // 3)} {__TAG__}"""
MARK0STARTLN = lambda __TAG__: f"""# {"0⟱ " * (CMNTLEN // 3)} {__TAG__}{NEWLINE}"""
MARK1END = lambda __TAG__: f"""# {"⟰1 " * (CMNTLEN // 3)} {__TAG__}"""
MARK1ENDLN = lambda __TAG__: f"""# {"⟰1 " * (CMNTLEN // 3)} {__TAG__}{NEWLINE}"""
MARK1MID = lambda __TAG__: f"""# {"⟰1⟱ " * (CMNTLEN // 4)} {__TAG__}"""
MARK1MIDLN = lambda __TAG__: f"""# {"⟰1⟱ " * (CMNTLEN // 4)} {__TAG__}{NEWLINE}"""
MARK1START = lambda __TAG__: f"""# {"1⟱ " * (CMNTLEN // 3)} {__TAG__}"""
MARK1STARTLN = lambda __TAG__: f"""# {"1⟱ " * (CMNTLEN // 3)} {__TAG__}{NEWLINE}"""
MARK2END = lambda __TAG__: f"""# {"⟰2 " * (CMNTLEN // 3)} {__TAG__}"""
MARK2ENDLN = lambda __TAG__: f"""# {"⟰2 " * (CMNTLEN // 3)} {__TAG__}{NEWLINE}"""
MARK2MID = lambda __TAG__: f"""# {"⟰2⟱ " * (CMNTLEN // 4)} {__TAG__}"""
MARK2MIDLN = lambda __TAG__: f"""# {"⟰2⟱ " * (CMNTLEN // 4)} {__TAG__}{NEWLINE}"""
MARK2START = lambda __TAG__: f"""# {"2⟱ " * (CMNTLEN // 3)} {__TAG__}"""
MARK2STARTLN = lambda __TAG__: f"""# {"2⟱ " * (CMNTLEN // 3)} {__TAG__}{NEWLINE}"""
MARK3END = lambda __TAG__: f"""# {"⟰3 " * (CMNTLEN // 3)} {__TAG__}"""
MARK3ENDLN = lambda __TAG__: f"""# {"⟰3 " * (CMNTLEN // 3)} {__TAG__}{NEWLINE}"""
MARK3MID = lambda __TAG__: f"""# {"⟰3⟱ " * (CMNTLEN // 4)} {__TAG__}"""
MARK3MIDLN = lambda __TAG__: f"""# {"⟰3⟱ " * (CMNTLEN // 4)} {__TAG__}{NEWLINE}"""
MARK3START = lambda __TAG__: f"""# {"3⟱ " * (CMNTLEN // 3)} {__TAG__}"""
MARK3STARTLN = lambda __TAG__: f"""# {"3⟱ " * (CMNTLEN // 3)} {__TAG__}{NEWLINE}"""
MARK4END = lambda __TAG__: f"""# {"⟰4 " * (CMNTLEN // 3)} {__TAG__}"""
MARK4ENDLN = lambda __TAG__: f"""# {"⟰4 " * (CMNTLEN // 3)} {__TAG__}{NEWLINE}"""
MARK4MID = lambda __TAG__: f"""# {"⟰4⟱ " * (CMNTLEN // 4)} {__TAG__}"""
MARK4MIDLN = lambda __TAG__: f"""# {"⟰4⟱ " * (CMNTLEN // 4)} {__TAG__}{NEWLINE}"""
MARK4START = lambda __TAG__: f"""# {"4⟱ " * (CMNTLEN // 3)} {__TAG__}"""
MARK4STARTLN = lambda __TAG__: f"""# {"4⟱ " * (CMNTLEN // 3)} {__TAG__}{NEWLINE}"""
MARK5END = lambda __TAG__: f"""# {"⟰5 " * (CMNTLEN // 3)} {__TAG__}"""
MARK5ENDLN = lambda __TAG__: f"""# {"⟰5 " * (CMNTLEN // 3)} {__TAG__}{NEWLINE}"""
MARK5MID = lambda __TAG__: f"""# {"⟰5⟱ " * (CMNTLEN // 4)} {__TAG__}"""
MARK5MIDLN = lambda __TAG__: f"""# {"⟰5⟱ " * (CMNTLEN // 4)} {__TAG__}{NEWLINE}"""
MARK5START = lambda __TAG__: f"""# {"5⟱ " * (CMNTLEN // 3)} {__TAG__}"""
MARK5STARTLN = lambda __TAG__: f"""# {"5⟱ " * (CMNTLEN // 3)} {__TAG__}{NEWLINE}"""
MARK6END = lambda __TAG__: f"""# {"⟰6 " * (CMNTLEN // 3)} {__TAG__}"""
MARK6ENDLN = lambda __TAG__: f"""# {"⟰6 " * (CMNTLEN // 3)} {__TAG__}{NEWLINE}"""
MARK6MID = lambda __TAG__: f"""# {"⟰6⟱ " * (CMNTLEN // 4)} {__TAG__}"""
MARK6MIDLN = lambda __TAG__: f"""# {"⟰6⟱ " * (CMNTLEN // 4)} {__TAG__}{NEWLINE}"""
MARK6START = lambda __TAG__: f"""# {"6⟱ " * (CMNTLEN // 3)} {__TAG__}"""
MARK6STARTLN = lambda __TAG__: f"""# {"6⟱ " * (CMNTLEN // 3)} {__TAG__}{NEWLINE}"""
MARK7END = lambda __TAG__: f"""# {"⟰7 " * (CMNTLEN // 3)} {__TAG__}"""
MARK7ENDLN = lambda __TAG__: f"""# {"⟰7 " * (CMNTLEN // 3)} {__TAG__}{NEWLINE}"""
MARK7MID = lambda __TAG__: f"""# {"⟰7⟱ " * (CMNTLEN // 4)} {__TAG__}"""
MARK7MIDLN = lambda __TAG__: f"""# {"⟰7⟱ " * (CMNTLEN // 4)} {__TAG__}{NEWLINE}"""
MARK7START = lambda __TAG__: f"""# {"7⟱ " * (CMNTLEN // 3)} {__TAG__}"""
MARK7STARTLN = lambda __TAG__: f"""# {"7⟱ " * (CMNTLEN // 3)} {__TAG__}{NEWLINE}"""
MARK8END = lambda __TAG__: f"""# {"⟰8 " * (CMNTLEN // 3)} {__TAG__}"""
MARK8ENDLN = lambda __TAG__: f"""# {"⟰8 " * (CMNTLEN // 3)} {__TAG__}{NEWLINE}"""
MARK8MID = lambda __TAG__: f"""# {"⟰8⟱ " * (CMNTLEN // 4)} {__TAG__}"""
MARK8MIDLN = lambda __TAG__: f"""# {"⟰8⟱ " * (CMNTLEN // 4)} {__TAG__}{NEWLINE}"""
MARK8START = lambda __TAG__: f"""# {"8⟱ " * (CMNTLEN // 3)} {__TAG__}"""
MARK8STARTLN = lambda __TAG__: f"""# {"8⟱ " * (CMNTLEN // 3)} {__TAG__}{NEWLINE}"""
MARK9END = lambda __TAG__: f"""# {"⟰9 " * (CMNTLEN // 3)} {__TAG__}"""
MARK9ENDLN = lambda __TAG__: f"""# {"⟰9 " * (CMNTLEN // 3)} {__TAG__}{NEWLINE}"""
MARK9MID = lambda __TAG__: f"""# {"⟰9⟱ " * (CMNTLEN // 4)} {__TAG__}"""
MARK9MIDLN = lambda __TAG__: f"""# {"⟰9⟱ " * (CMNTLEN // 4)} {__TAG__}{NEWLINE}"""
MARK9START = lambda __TAG__: f"""# {"9⟱ " * (CMNTLEN // 3)} {__TAG__}"""
MARK9STARTLN = lambda __TAG__: f"""# {"9⟱ " * (CMNTLEN // 3)} {__TAG__}{NEWLINE}"""


MARK_END = lambda __TAG__: f"""# {__TAG__} {"⟰ " * (CMNTLEN // 2)}"""
MARK_ENDLN = lambda __TAG__: f"""# {__TAG__} {"⟰ " * (CMNTLEN // 2)}{NEWLINE}"""
MARK_MID = lambda __TAG__: f"""# {__TAG__} {"⟰⟱" * (CMNTLEN // 2)}"""
MARK_MIDLN = lambda __TAG__: f"""# {__TAG__} {"⟰⟱" * (CMNTLEN // 2)}{NEWLINE}"""
MARK_START = lambda __TAG__: f"""# {__TAG__} {" ⟱" * (CMNTLEN // 2)}"""
MARK_STARTLN = lambda __TAG__: f"""# {__TAG__} {" ⟱" * (CMNTLEN // 2)}{NEWLINE}"""


# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# makeAComment
# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
def makeAComment(
		comment_,
):
	# fold here ⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1
	_strToRtn_ = ""
	_strToRtn_ += f"""{CMNTLINE}{NEWLINE}# * {comment_}{NEWLINE}{CMNTLINE}{NEWLINE}"""
	return _strToRtn_
	# fold here ⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1


# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# makeAComment
# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
def makeAWideComment(
		comment_,
):
	# fold here ⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1
	_strToRtn_ = ""
	_strToRtn_ += f"""#{NEWLINE}#{NEWLINE}{CMNTLINE}{NEWLINE}# * {comment_}{NEWLINE}{CMNTLINE}{NEWLINE}#{NEWLINE}#{NEWLINE}"""
	return _strToRtn_
	# fold here ⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1


#


#
#
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# start of CSCF.CONST_D.MARKERS
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
#
#
