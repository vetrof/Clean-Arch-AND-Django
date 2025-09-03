from unittest.mock import Mock
from app_products.service import ProductService
from app_products.models import Product

def test_service_calls_have_discount_real_product():
    # Настоящая модель (но БД не трогаем!)
    product = Product(name="Test", price=150)

    repo = Mock()
    repo.get_by_id.return_value = product

    service = ProductService(repo)

    result, flag = service.get_product(1)

    assert result == product
    assert flag is True
