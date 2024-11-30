##
## Auto Generated makefile by CodeLite IDE
## any manual changes will be erased      
##
## Debug
ProjectName            :=HomEWork_3
ConfigurationName      :=Debug
WorkspaceConfiguration :=Debug
WorkspacePath          :="C:/Users/Kaan Yalman/Section4/Midterm"
ProjectPath            :="C:/Users/Kaan Yalman/Section4/Midterm/HomEWork_3"
IntermediateDirectory  :=$(ConfigurationName)
OutDir                 := $(IntermediateDirectory)
CurrentFileName        :=
CurrentFilePath        :=
CurrentFileFullPath    :=
User                   :=Kaan Yalman
Date                   :=6/4/2023
CodeLitePath           :="C:/Program Files/CodeLite"
LinkerName             :=C:/mingw64/bin/g++.exe
SharedObjectLinkerName :=C:/mingw64/bin/g++.exe -shared -fPIC
ObjectSuffix           :=.o
DependSuffix           :=
PreprocessSuffix       :=.i
DebugSwitch            :=-g 
IncludeSwitch          :=-I
LibrarySwitch          :=-l
OutputSwitch           :=-o 
LibraryPathSwitch      :=-L
PreprocessorSwitch     :=-D
SourceSwitch           :=-c 
OutputDirectory        :=$(IntermediateDirectory)
OutputFile             :=$(IntermediateDirectory)/$(ProjectName).exe
Preprocessors          :=
ObjectSwitch           :=-o 
ArchiveOutputSwitch    := 
PreprocessOnlySwitch   :=-E
ObjectsFileList        :="HomEWork_3.txt"
PCHCompileFlags        :=
MakeDirCommand         :=makedir
RcCmpOptions           := 
RcCompilerName         :=C:/mingw64/bin/windres.exe
LinkOptions            :=  -static
IncludePath            :=  $(IncludeSwitch). $(IncludeSwitch). 
IncludePCH             := 
RcIncludePath          := 
Libs                   := 
ArLibs                 :=  
LibPath                := $(LibraryPathSwitch). 

##
## Common variables
## AR, CXX, CC, AS, CXXFLAGS and CFLAGS can be overridden using an environment variable
##
AR       := C:/mingw64/bin/ar.exe -r
CXX      := C:/mingw64/bin/g++.exe
CC       := C:/mingw64/bin/gcc.exe
CXXFLAGS :=  -g -O0 -gdwarf-2 -std=c++17 -Wall $(Preprocessors)
CFLAGS   :=  -gdwarf-2 -O0 -Wall $(Preprocessors)
ASFLAGS  := 
AS       := C:/mingw64/bin/as.exe


##
## User defined environment variables
##
CodeLiteDir:=C:\Program Files\CodeLite
Objects0=$(IntermediateDirectory)/Circle.cpp$(ObjectSuffix) $(IntermediateDirectory)/main.cpp$(ObjectSuffix) $(IntermediateDirectory)/Square.cpp$(ObjectSuffix) $(IntermediateDirectory)/Shape.cpp$(ObjectSuffix) $(IntermediateDirectory)/PlanarShape.cpp$(ObjectSuffix) $(IntermediateDirectory)/VolumetricShape.cpp$(ObjectSuffix) $(IntermediateDirectory)/Cube.cpp$(ObjectSuffix) $(IntermediateDirectory)/Sphere.cpp$(ObjectSuffix) 



Objects=$(Objects0) 

##
## Main Build Targets 
##
.PHONY: all clean PreBuild PrePreBuild PostBuild MakeIntermediateDirs
all: $(OutputFile)

$(OutputFile): $(IntermediateDirectory)/.d $(Objects) 
	@$(MakeDirCommand) $(@D)
	@echo "" > $(IntermediateDirectory)/.d
	@echo $(Objects0)  > $(ObjectsFileList)
	$(LinkerName) $(OutputSwitch)$(OutputFile) @$(ObjectsFileList) $(LibPath) $(Libs) $(LinkOptions)

MakeIntermediateDirs:
	@$(MakeDirCommand) "$(ConfigurationName)"


$(IntermediateDirectory)/.d:
	@$(MakeDirCommand) "$(ConfigurationName)"

PreBuild:


##
## Objects
##
$(IntermediateDirectory)/Circle.cpp$(ObjectSuffix): Circle.cpp
	$(CXX) $(IncludePCH) $(SourceSwitch) "C:/Users/Kaan Yalman/Section4/Midterm/HomEWork_3/Circle.cpp" $(CXXFLAGS) $(ObjectSwitch)$(IntermediateDirectory)/Circle.cpp$(ObjectSuffix) $(IncludePath)
$(IntermediateDirectory)/Circle.cpp$(PreprocessSuffix): Circle.cpp
	$(CXX) $(CXXFLAGS) $(IncludePCH) $(IncludePath) $(PreprocessOnlySwitch) $(OutputSwitch) $(IntermediateDirectory)/Circle.cpp$(PreprocessSuffix) Circle.cpp

$(IntermediateDirectory)/main.cpp$(ObjectSuffix): main.cpp
	$(CXX) $(IncludePCH) $(SourceSwitch) "C:/Users/Kaan Yalman/Section4/Midterm/HomEWork_3/main.cpp" $(CXXFLAGS) $(ObjectSwitch)$(IntermediateDirectory)/main.cpp$(ObjectSuffix) $(IncludePath)
$(IntermediateDirectory)/main.cpp$(PreprocessSuffix): main.cpp
	$(CXX) $(CXXFLAGS) $(IncludePCH) $(IncludePath) $(PreprocessOnlySwitch) $(OutputSwitch) $(IntermediateDirectory)/main.cpp$(PreprocessSuffix) main.cpp

$(IntermediateDirectory)/Square.cpp$(ObjectSuffix): Square.cpp
	$(CXX) $(IncludePCH) $(SourceSwitch) "C:/Users/Kaan Yalman/Section4/Midterm/HomEWork_3/Square.cpp" $(CXXFLAGS) $(ObjectSwitch)$(IntermediateDirectory)/Square.cpp$(ObjectSuffix) $(IncludePath)
$(IntermediateDirectory)/Square.cpp$(PreprocessSuffix): Square.cpp
	$(CXX) $(CXXFLAGS) $(IncludePCH) $(IncludePath) $(PreprocessOnlySwitch) $(OutputSwitch) $(IntermediateDirectory)/Square.cpp$(PreprocessSuffix) Square.cpp

$(IntermediateDirectory)/Shape.cpp$(ObjectSuffix): Shape.cpp
	$(CXX) $(IncludePCH) $(SourceSwitch) "C:/Users/Kaan Yalman/Section4/Midterm/HomEWork_3/Shape.cpp" $(CXXFLAGS) $(ObjectSwitch)$(IntermediateDirectory)/Shape.cpp$(ObjectSuffix) $(IncludePath)
$(IntermediateDirectory)/Shape.cpp$(PreprocessSuffix): Shape.cpp
	$(CXX) $(CXXFLAGS) $(IncludePCH) $(IncludePath) $(PreprocessOnlySwitch) $(OutputSwitch) $(IntermediateDirectory)/Shape.cpp$(PreprocessSuffix) Shape.cpp

$(IntermediateDirectory)/PlanarShape.cpp$(ObjectSuffix): PlanarShape.cpp
	$(CXX) $(IncludePCH) $(SourceSwitch) "C:/Users/Kaan Yalman/Section4/Midterm/HomEWork_3/PlanarShape.cpp" $(CXXFLAGS) $(ObjectSwitch)$(IntermediateDirectory)/PlanarShape.cpp$(ObjectSuffix) $(IncludePath)
$(IntermediateDirectory)/PlanarShape.cpp$(PreprocessSuffix): PlanarShape.cpp
	$(CXX) $(CXXFLAGS) $(IncludePCH) $(IncludePath) $(PreprocessOnlySwitch) $(OutputSwitch) $(IntermediateDirectory)/PlanarShape.cpp$(PreprocessSuffix) PlanarShape.cpp

$(IntermediateDirectory)/VolumetricShape.cpp$(ObjectSuffix): VolumetricShape.cpp
	$(CXX) $(IncludePCH) $(SourceSwitch) "C:/Users/Kaan Yalman/Section4/Midterm/HomEWork_3/VolumetricShape.cpp" $(CXXFLAGS) $(ObjectSwitch)$(IntermediateDirectory)/VolumetricShape.cpp$(ObjectSuffix) $(IncludePath)
$(IntermediateDirectory)/VolumetricShape.cpp$(PreprocessSuffix): VolumetricShape.cpp
	$(CXX) $(CXXFLAGS) $(IncludePCH) $(IncludePath) $(PreprocessOnlySwitch) $(OutputSwitch) $(IntermediateDirectory)/VolumetricShape.cpp$(PreprocessSuffix) VolumetricShape.cpp

$(IntermediateDirectory)/Cube.cpp$(ObjectSuffix): Cube.cpp
	$(CXX) $(IncludePCH) $(SourceSwitch) "C:/Users/Kaan Yalman/Section4/Midterm/HomEWork_3/Cube.cpp" $(CXXFLAGS) $(ObjectSwitch)$(IntermediateDirectory)/Cube.cpp$(ObjectSuffix) $(IncludePath)
$(IntermediateDirectory)/Cube.cpp$(PreprocessSuffix): Cube.cpp
	$(CXX) $(CXXFLAGS) $(IncludePCH) $(IncludePath) $(PreprocessOnlySwitch) $(OutputSwitch) $(IntermediateDirectory)/Cube.cpp$(PreprocessSuffix) Cube.cpp

$(IntermediateDirectory)/Sphere.cpp$(ObjectSuffix): Sphere.cpp
	$(CXX) $(IncludePCH) $(SourceSwitch) "C:/Users/Kaan Yalman/Section4/Midterm/HomEWork_3/Sphere.cpp" $(CXXFLAGS) $(ObjectSwitch)$(IntermediateDirectory)/Sphere.cpp$(ObjectSuffix) $(IncludePath)
$(IntermediateDirectory)/Sphere.cpp$(PreprocessSuffix): Sphere.cpp
	$(CXX) $(CXXFLAGS) $(IncludePCH) $(IncludePath) $(PreprocessOnlySwitch) $(OutputSwitch) $(IntermediateDirectory)/Sphere.cpp$(PreprocessSuffix) Sphere.cpp

##
## Clean
##
clean:
	$(RM) -r $(ConfigurationName)/


