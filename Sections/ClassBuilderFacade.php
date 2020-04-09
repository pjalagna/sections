<?php
// file ClassBuilderFacade.php
/*
09-08-2018 wip - edits
09-07-2018 wip
09-05-2018 wip
09-04-2018 pja original

methods
ClassMaker
initClass
addProperty
addMethod
pout

notes uses sectionsClass to aid builder in creating a php class
*/
function ClassBuilderFacadeHelp() {
$ans = <<< sa
methods are:
initFacade -> new sections (tst)
ClassMaker == produces class file from tuple
-- (switch,
---- "N" or "" == new class to be created
---- "A" == append or add properties and/or processes to know class file
-- ClassName,
-- propertiesArray,
-- processArray,
-- FileName)
// method addProperty (auto adds get_set)
// method addProcess
//  method pout - print finished class
// method fout(fna) - print finished class to file
dumptst($tst)
sa
;
echo ($ans);
} // end-ClassBuilderFacadeHelp
function ClassMaker($switch,$ClassName,$propertiesArray,$processArray,$FileName) {
    // builds class file from tuple

} // end-ClassMaker
function initFacade(){
require_once 'SectionsClass.php';
$tst = new Sections;
// main
// build the templates
$tst->NameSection('ClassHeadT');
$d = <<< d1
class %cna {
d1
;
$tst->writeSection('ClassHeadT',$d);
// properties
$tst->NameSection('propertiesT');
$d = <<< d1
    private $%pna = '';
d1
;
$tst->writeSection('propertiesT',$d);
// get_set
$tst->NameSection('get_setT');
$d = <<<'d1'
    public function get_%pna () {
        return($this->%pna);
    } // end-get_%pna
    public functionset_%pna (%val) {
        $this->%pna = %val;
    } // end-set_%pna
    
d1;
$tst->writeSection('get_setT',$d);
// methodsT
$tst->NameSection('methodsT');
$tst->writeSection('methodsT','');
// tailT
$tst->NameSection('tailT');
$d = <<<'d1'
} // end-Class %cna
d1;
$tst->writeSection('tailT',$d);
return($tst);
}
function initClass($cna,$tst) {
// -- build holding sections
$tst->NameSection('ClassHead'); 
// fill in
$tst->NameSection('properties');
$tst->NameSection('get_set'); 
$tst->NameSection('process');
$tst->NameSection('ClassTail');   
// ---- head,properties, get_sets,process,tail
} // end-initClass
// method addProperty (auto adds get_set)
// method addProcess
//  method pout - print finished class
// method fout(fna) - print finished class to file
function dumptst($tst){
var_dump($tst);
}
?>

