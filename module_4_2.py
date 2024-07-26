def test_function():
    def inner_function():
        print("Я в области видимости функции test_function")
    inner_function()  # не возвращает
inner_function() # выдает ошибку
test_function() # работает