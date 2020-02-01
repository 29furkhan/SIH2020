function clickFilters(id){
    document.getElementById(id).style.display = "block";
}

function getUserType(type){
    type = document.getElementById(type).value;

    if(type=="alumni" || type=="student")
    {
        document.getElementById('PRN_NO').style.display="table-row";
        if(type=="alumni" || type=="student")
        {
            document.getElementById('collegeselecttr').style.display="table-row";
            document.getElementById('dircollegeselect').style.display="none";
        }
        else if(type="DIR"){
            document.getElementById('dircollegeselect').style.display="table-row";
            document.getElementById('collegeselecttr').style.display="none";
        }
        else if(type="DHE"){
            document.getElementById('userid').style.display="table-row";
            document.getElementById('password').style.display="table-row";
        }
    }

}
