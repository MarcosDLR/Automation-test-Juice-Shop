import os

class Screen_shot():

    def take_screenshot(driver,module,name):
        directory = os.getcwd() + "/screenshots/" + module
        if not os.path.exists(directory):
            os.makedirs(directory)

        file_name = f"{name}.png"
        file_path = f"{directory}/{file_name}"
        
        driver.save_screenshot(file_path)