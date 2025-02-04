# SQLAL chemy에서 데이터베이스 연결을 위한 모듈 가져오기
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#MYSQL 데이터베이스 연결 설정
# "mysql+pymysql://사용자이름:비밀번호@호스트:포트/데이터베이스"
DATABASE_URL = "mysql+pymysql://root:1234@localhost:3308/mydb"

# SQLALchemy 의 엔진 생성
# 데이터에비으솨의 연결을 관리하는 객체
# 해당 엔진을 통해 SQL 실행 및 ORM 기능 활용 가능
engine = create_engine(DATABASE_URL)

#세션(Session) 생성
#데이터베이스와의 연결을 관리하는 세션 팩토리 생성
#autocommit=False: 자동 커밋 비활성화(트랜잭션 수동 관리)
#autoflush=False: 자동 플러시 비활성화(세션의 변경 사항을 즉시 반영하지 않음)
#bind=engine: 생성된 엔진을 세션에 연결
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# ORM을 위한 기본 클래스 생성
# declarative_base()를 통해 데이터베이스 모델을 정의할 때 사용할 Base 클래스 생성
# 이 클래스를 상속받아 데이터 모델(테이블)을 정의
Base = declarative_base()