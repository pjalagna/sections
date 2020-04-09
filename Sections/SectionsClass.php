<?php
// file SectionsClass.php
/*
09-04-2018 pja original
*/
class Sections {
   // properties
   private $sectionsAr = array();
   // methods
   public function NameSection($sna) {
       $this->sectionsAr[$sna] = ''; // create the section
   } // end-NameSection
   public function writeSection($sna,$sval){
       $this->sectionsAr[$sna] = $this->sectionsAr[$sna] . '<br />' . $sval; // append
   } // end-writeSection
   public function readSection($sna){
       return($this->sectionsAr[$sna]);
   } // end-readSection

} // endClass Sections

?>

