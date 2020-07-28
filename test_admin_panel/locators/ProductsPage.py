class ProductsPage:
    Top_checkbox = ".table > tbody:nth-child(2) > tr:nth-child(1) > td:nth-child(1) > input:nth-child(1)"
    Catalog = "menu-catalog"
    Product = "Products"
    Delete_button = "button.btn:nth-child(4)"
    Add_button = "a.btn:nth-child(2)"
    Product_name_input = "#input-name1"
    Description_input = ".note-editable"
    Meta_teg_title_input = "#input-meta-title1"
    Data_page = "#form-product > ul:nth-child(1) > li:nth-child(2) > a:nth-child(1)"
    Model_input = "#input-model"
    Save_button = "div.pull-right > button:nth-child(1)"
    Modify_button = ".table > tbody:nth-child(2) > tr:nth-child(1) > td:nth-child(8) > a:nth-child(1)"
    Product_info = {
        "Product name": "test",
        "Description": "This is test product added by Selenium",
        "Meta teg title": "TEST"
    }
    Data = {
        "Model": "Selenium 1.0"
    }
