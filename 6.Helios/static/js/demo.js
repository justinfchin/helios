/*
 * Author: Justin Chin
 * 
 */

var filterID=-1; // ID Filter
var selectedFilter; // current selected filtered on GUI
var filters = ["","wiener","butter","rnn"]; // list of different filters

// For Updating Audio Clip
function updateClip(){
    
}

// For Changing Filter Applied to the Audio
function setFilter(newFilterID, item){
    // Check if item is currently selected
    if (filterID == newFilterID) return;

    // Update the filterID
    filterID = newFilterID;

    // Remove old selected in GUI
    if (selectedFilter) selectedFilter.classList.remove("selected");

    // Make the selected item selected in GUI & Update new selected Filter    
    item.classList.add("selected");
    selectedFilter = item;

    // Update Audio based on this
    updateClip()
}
