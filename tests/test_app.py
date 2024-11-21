from streamlit_db_demo.app import create_app_config, TITLE

def test_create_app_config() -> None:
    config = create_app_config()
    assert config.title == TITLE
