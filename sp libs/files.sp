func fopen(filename, text_, mode_) -> wf1daffl(filename, text_, mode_)
func fwrite(filename, text_) -> wf1daffl(filename, text_, "w")
func fappend(filename, text_) -> wf1daffl(filename, text_, "a")
func fcls(filename) -> wf1daffl(filename, "", "w")
func fread(filename) -> rf1daffl(filename)

func file.exists(filename) -> ex1daffl(filename)
func frename(filename, new_name) -> rnf1dffl(filename, new_name)
func fcreate(filename) -> wf1daffl(filename, "", "x")
func fdelete(filename) -> df1daffl(filename)
func fremove(filename) -> fdelete(filename)