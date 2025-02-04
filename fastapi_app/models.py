# SQLALchemy 에서 테이블을 정의하는데 필요한 모듈 가져오기
from sqlalchemy import Column, BigInteger, String

# 이전에 생성한 'Base'클래스를 가져오기(ORM 모델의 기반 클래스)
from database import Base

# Users 테이블을 정의하는 ORM 모델 클래스
class User(Base):
  __tablename__ = "users"

# 'id' 컬럼 정의(BIGINT(Long), 기본키, 인덱스 추가)
  id = Column(BigInteger, primary_key=True, index=True)
  name = Column(String, nullable = False)